#!/usr/bin/env python3
"""
Citation Verification & BibTeX Management Tool (für gpunkt.org Wörterbuch)

Findet alle Citekeys in Wörterbuch-Einträgen, vergleicht mit bibliography.bib.
Identifiziert fehlende Quellen und generiert Import-Datei für Zotero.

Workflow:
1. Skript findet fehlende Citekeys (@autor_jahr).
2. Skript generiert Stubs in 'wort-fabrik/imports/to_zotero.bib'.
3. User importiert diese Datei in Zotero (File -> Import -> BibTeX).
4. User vervollständigt Metadaten in Zotero (Magic Wand / Manuell).
5. Zotero exportiert saubere 'bibliography.bib'.

Usage:
    python verify_citations.py              # Nur prüfen
    python verify_citations.py --fix        # Stubs in to_zotero.bib schreiben
    python verify_citations.py --verbose    # Details anzeigen

WICHTIG: Dieses Skript ist für politische Primärquellen optimiert.
         Alle generierten Stubs MÜSSEN triple-verified werden!
"""

import os
import re
import sys
from pathlib import Path
from typing import Set, Dict, List, Tuple
import argparse


# Konfiguration
ZETTELKASTEN_DIR = Path(__file__).parent.parent
BIBLIOGRAPHY_FILE = ZETTELKASTEN_DIR / "bibliography.bib"
IMPORTS_DIR = ZETTELKASTEN_DIR / "wort-fabrik" / "imports"
TO_ZOTERO_FILE = IMPORTS_DIR / "to_zotero.bib"
EXCLUDE_FILES = ["README.md", "index.md", "CLAUDE.md"]


def extract_citekeys_from_file(filepath: Path) -> Set[str]:
    """Extrahiert alle Citekeys (@author_year) aus einer Datei."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all @citekeys (format: @author_year or @author_year_word)
    # Ignore @book, @article etc. (BibTeX types)
    citekeys = re.findall(r'@([a-z][a-z_0-9]+)', content, re.IGNORECASE)

    bibtex_types = {'book', 'article', 'incollection', 'inproceedings', 'misc', 'phdthesis', 'mastersthesis', 'online', 'report'}
    return {ck for ck in citekeys if ck.lower() not in bibtex_types}


def extract_citekeys_from_zettels() -> Dict[str, Set[str]]:
    """Scannt alle Wörterbuch-Einträge und extrahiert Citekeys."""
    citekeys_by_file = {}
    md_files = list(ZETTELKASTEN_DIR.glob("*.md"))

    for filepath in md_files:
        if filepath.name in EXCLUDE_FILES:
            continue

        citekeys = extract_citekeys_from_file(filepath)
        if citekeys:
            citekeys_by_file[filepath.name] = citekeys

    return citekeys_by_file


def extract_citekeys_from_bibliography() -> Set[str]:
    """Extrahiert alle Citekeys aus bibliography.bib."""
    if not BIBLIOGRAPHY_FILE.exists():
        return set()

    with open(BIBLIOGRAPHY_FILE, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex für BibTeX Entries: @type{citekey,
    entries = re.findall(r'@(?:book|article|incollection|inproceedings|misc|phdthesis|mastersthesis|online|report)\{([^,]+)', content)
    return set(entries)


def parse_citekey(citekey: str) -> Dict[str, str]:
    """Parsed Citekey (author_year) für Stub-Generierung."""
    parts = citekey.split('_')

    # Simple Heuristic
    if len(parts) >= 2 and parts[-1].isdigit():
        year = parts[-1]
        author = " ".join(parts[:-1]).title()
    else:
        year = "???? (TODO)"
        author = citekey.title()

    return {'citekey': citekey, 'author': author, 'year': year}


def generate_bibtex_stub(citekey: str) -> str:
    """Generiert einen BibTeX-Stub für Zotero Import."""
    meta = parse_citekey(citekey)
    return f"""@misc{{{meta['citekey']},
  title = {{{{TODO: Quelle für {meta['citekey']} finden}}}},
  author = {{{meta['author']}}},
  year = {{{meta['year']}}},
  note = {{{{gpunkt.org Import Stub - Triple-Verification erforderlich!}}}}
}}
"""


def find_missing_citations() -> Tuple[Set[str], Dict[str, List[str]]]:
    """Vergleicht Wörterbuch-Citations mit Bibliography."""
    citekeys_by_file = extract_citekeys_from_zettels()
    all_citekeys = set().union(*citekeys_by_file.values()) if citekeys_by_file else set()
    bib_citekeys = extract_citekeys_from_bibliography()

    missing = all_citekeys - bib_citekeys

    missing_by_file = {}
    for filepath, keys in citekeys_by_file.items():
        file_missing = keys & missing
        if file_missing:
            missing_by_file[filepath] = sorted(file_missing)

    return missing, missing_by_file


def write_to_zotero_import(stubs: List[str]):
    """Schreibt Stubs in to_zotero.bib (Append Mode)."""
    if not stubs: return

    # Ensure directory exists
    IMPORTS_DIR.mkdir(parents=True, exist_ok=True)

    with open(TO_ZOTERO_FILE, 'a', encoding='utf-8') as f:
        f.write("\n")
        for stub in stubs:
            f.write(stub + "\n")

    print(f"\n✅ {len(stubs)} Stubs in '{TO_ZOTERO_FILE.name}' geschrieben.")
    print(f"\n⚠️  KRITISCH: TRIPLE-VERIFICATION erforderlich!")
    print(f"    Jede Quelle MUSS 3x geprüft werden (siehe RECHERCHE-ZITATE.md)")
    print(f"\n🚀 NÄCHSTE SCHRITTE:")
    print(f"1. Öffne Zotero")
    print(f"2. File -> Import -> '{TO_ZOTERO_FILE}'")
    print(f"3. Vervollständige die Daten (Recherche-Dateien nutzen!)")
    print(f"4. TRIPLE-VERIFY: Link öffnen + Wort-für-Wort prüfen + Metadaten abgleichen")
    print(f"5. Better BibTeX Export -> Überschreibe '{BIBLIOGRAPHY_FILE.name}'")


def main():
    parser = argparse.ArgumentParser(description="Citation Verification & Zotero Bridge (gpunkt.org)")
    parser.add_argument('--fix', '-f', action='store_true', help='Generiert Stubs in to_zotero.bib')
    parser.add_argument('--verbose', '-v', action='store_true', help='Mehr Details')
    args = parser.parse_args()

    print("🔍 Scanne Wörterbuch-Einträge nach fehlenden Quellen...")
    missing, missing_by_file = find_missing_citations()

    if not missing:
        print("\n✅ Alle Quellen sind in bibliography.bib vorhanden.")
        return 0

    print(f"\n❌ {len(missing)} fehlende Quellen gefunden:\n")

    # Show where they are missing
    for filepath, keys in sorted(missing_by_file.items()):
        print(f"📄 {filepath}:")
        for k in keys: print(f"   - @{k}")
        print()

    if args.fix:
        print(f"🛠️  Generiere Import-Stubs für Zotero...")
        stubs = [generate_bibtex_stub(k) for k in sorted(missing)]
        write_to_zotero_import(stubs)
    else:
        print(f"💡 Tipp: Nutze 'python3 wort-fabrik/verify_citations.py --fix' zum Generieren der Import-Datei.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
