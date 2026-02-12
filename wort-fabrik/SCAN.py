#!/usr/bin/env python3
"""
DIP Discovery v4 - Erweitertes Zitatformat mit TOP-Titeln und Seitenangaben

Verbesserungen gegenüber v3:
- TOP-Titel aus XML: jeder BibTeX-Eintrag bekommt den echten Tagesordnungspunkt
- Seitenbereich-Extraktion (best-effort): pages = {7012A--7014C}
- Neue BibTeX-Felder: address, organization, number, pages
- pages wird weggelassen wenn nicht extrahierbar (kein leerer Eintrag)
- Skalierbar für Landtage + Europaparlament (address/organization als Parameter)

USAGE:
    python3 SCAN.py "Begriff"
    python3 SCAN.py "Begriff" 2010  # optional: Startjahr

BEISPIELE:
    python3 SCAN.py "Sozialtourismus"
    python3 SCAN.py "Remigration" 2018
"""

import sys
import json
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import re
from datetime import datetime

API_KEY = "OSOegLs.PR2lwJ1dwCeje9vTj7FPOt3hvpYKtwKkhw"
BASE_URL = "https://search.dip.bundestag.de/api/v1"
MAX_PER_YEAR = 5  # Maximal 5 Treffer pro Jahr


def generate_citekey(nachname, jahr, monat, tag):
    """Generiert Citekey: nachname_jahr_monat_tag (lowercase, keine Umlaute, zero-padded)
    Entspricht der Zotero Better BibTeX Formel: auth.lower + "_" + date('%Y_%m_%d')
    """
    nachname_clean = nachname.lower()
    nachname_clean = nachname_clean.replace('ä', 'ae').replace('ö', 'oe')
    nachname_clean = nachname_clean.replace('ü', 'ue').replace('ß', 'ss')
    nachname_clean = re.sub(r'[^a-z]', '', nachname_clean)
    return f"{nachname_clean}_{jahr}_{monat:02d}_{tag:02d}"


def extract_context_around_paragraph(rede_elem, target_p, term):
    """Extrahiert Ziel-Absatz + ggf. nächsten kurzen Absatz als Kontext."""
    paragraphs = []
    found = False

    for p in rede_elem.findall('.//p'):
        if p.get('klasse') not in ['J', 'J_1', 'O']:
            continue
        text = ' '.join(''.join(p.itertext()).split()).strip()
        if p == target_p:
            found = True
            paragraphs.append(text)
        elif found and len(paragraphs) == 1:
            if len(text) < 300:
                paragraphs.append(text)
            break

    context = '  '.join(paragraphs)
    # Führende Artefakte (Gedankenstriche, Leerzeichen)
    context = re.sub(r'^[–\-\s]+', '', context).strip()
    # Satzzeichen-Cluster in der Mitte glätten (z.B. ,. → .)
    context = re.sub(r',([.!?])', r'\1', context)
    context = re.sub(r'[–\-]([.!?])', r'\1', context)
    # Cluster am Ende bereinigen (z.B. –,. → . oder –, → [wegfallen])
    context = re.sub(r'[\-–,;:\s]+([.!?])$', r'\1', context)
    context = re.sub(r'[\-–,;:]+\s*$', '', context).strip()
    if context and not context.endswith(('.', '!', '?', '\u201c')):
        context += '.'
    return context


def extract_top_title(rede_elem, parent_map):
    """Extrahiert den Tagesordnungspunkt-Titel für eine Rede."""
    current = rede_elem
    top_elem = None

    for _ in range(10):
        parent = parent_map.get(current)
        if parent is None:
            break
        if parent.tag == 'tagesordnungspunkt':
            top_elem = parent
            break
        current = parent

    if top_elem is None:
        return ""

    # Alle <p>-Titel-Elemente vor dem ersten <rede>-Element sammeln
    title_parts = []
    for child in top_elem:
        if child.tag == 'rede':
            break
        if child.tag == 'p':
            klasse = child.get('klasse', '')
            if klasse in ['T_BT_fett', 'T', 'T_NaS', 'T_BT']:
                text = ' '.join(''.join(child.itertext()).split()).strip()
                # Strukturlabels überspringen: reine Ziffern, "Tagesordnungspunkt N:", "TOP N:"
                if text and not re.match(r'^(Tagesordnungspunkt\s+|TOP\s+)?\d+:?\s*$', text, re.IGNORECASE):
                    title_parts.append(text)

    if not title_parts:
        return ""

    title = ' '.join(title_parts)
    # Führende Ziffer entfernen (z.B. "2 Erste Beratung..." → "Erste Beratung...")
    title = re.sub(r'^\d+\s+', '', title)
    # Abschließenden Doppelpunkt entfernen
    title = title.rstrip(': \t')
    # Ersten Buchstaben großschreiben (Fragmente wie "auf Verlangen..." → "Auf Verlangen...")
    if title:
        title = title[0].upper() + title[1:]
    return title


def extract_page_range(rede_elem):
    """
    Versucht, den Seitenbereich (Protokoll-Spalten) einer Rede zu extrahieren.
    Format: 7012A--7014C (erste und letzte Spaltenangabe in der Rede).
    Best-effort: gibt leeren String zurück wenn nicht gefunden.
    """
    page_pattern = re.compile(r'\b(\d{4,5})\s*([A-D])\b')
    full_text = ''.join(rede_elem.itertext())
    matches = page_pattern.findall(full_text)

    if not matches:
        return ""

    first = f"{matches[0][0]}{matches[0][1]}"
    last = f"{matches[-1][0]}{matches[-1][1]}"

    if first == last:
        return first
    return f"{first}--{last}"


def parse_xml_for_term(xml_url, term):
    """
    Parst XML-Protokoll und gibt alle Reden zurück, die den Begriff enthalten.
    Gibt strukturierte Daten mit Sprecher, Rolle, TOP-Titel, Seiten und Kontext zurück.
    """
    try:
        with urllib.request.urlopen(xml_url, timeout=30) as response:
            xml_data = response.read()
        root = ET.fromstring(xml_data)

        # Parent-Map für Aufwärts-Traversierung (TOP-Titel-Extraktion)
        parent_map = {c: p for p in root.iter() for c in p}

        results = []

        for rede in root.findall('.//rede'):
            redner_elem = rede.find('.//redner')
            if redner_elem is None:
                continue

            person_id = redner_elem.get('id', '')
            name_elem = redner_elem.find('name')
            if name_elem is None:
                continue

            vorname_e = name_elem.find('vorname')
            nachname_e = name_elem.find('nachname')
            fraktion_e = name_elem.find('fraktion')
            rolle_e = name_elem.find('rolle/rolle_lang')

            vorname = vorname_e.text if vorname_e is not None else ""
            nachname = nachname_e.text if nachname_e is not None else "Unbekannt"
            fraktion = fraktion_e.text if fraktion_e is not None else ""
            rolle = ' '.join(rolle_e.text.split()) if rolle_e is not None else ""

            top_title = extract_top_title(rede, parent_map)

            # Suche Begriff in Absätzen
            for p in rede.findall('.//p'):
                if p.get('klasse') not in ['J', 'J_1', 'O']:
                    continue
                text = ''.join(p.itertext())
                if term.lower() in text.lower():
                    context = extract_context_around_paragraph(rede, p, term)
                    pages = extract_page_range(rede)
                    results.append({
                        'vorname': vorname,
                        'nachname': nachname,
                        'fraktion': fraktion,
                        'rolle': rolle,
                        'context': context,
                        'top_title': top_title,
                        'pages': pages,
                        'person_id': person_id,
                    })
                    break  # Nur ersten Treffer pro Rede

        return results

    except Exception as e:
        print(f"  ⚠️  XML-Fehler: {e}", file=sys.stderr)
        return []


def generate_bibtex(nachname, vorname, jahr, monat, tag, wp, dok_nr, pdf_url, citekey,
                    rolle="", top_title="", pages="", person_id="",
                    address="Berlin", organization="Deutscher Bundestag"):
    """Generiert BibTeX-Eintrag nach akademischem Standard (CITING_STANDARDS.md)."""
    if top_title:
        titel = top_title
    elif rolle:
        titel = f"Rede im Deutschen Bundestag als {rolle} (Plenarprotokoll {wp}/{dok_nr})"
    else:
        titel = f"Rede im Deutschen Bundestag (Plenarprotokoll {wp}/{dok_nr})"

    shorttitle = titel[:77].strip() + "..." if len(titel) > 80 else titel
    note = f"Plenarprotokoll {wp}/{dok_nr}"

    lines = [
        f"@misc{{{citekey},",
        f"  title = {{{titel}}},",
        f"  shorttitle = {{{shorttitle}}},",
        f"  author = {{{nachname}, {vorname}}},",
        f"  year = {{{jahr}}},",
        f"  month = {{{monat}}},",
        f"  day = {{{tag}}},",
        f"  address = {{{address}}},",
        f"  organization = {{{organization}}},",
        f"  number = {{{wp}/{dok_nr}}},",
        f"  langid = {{german}},",
    ]
    if person_id:
        lines.append(f"  keywords = {{person_id:{person_id}}},")
    if pages:
        lines.append(f"  pages = {{{pages}}},")
    lines += [
        f"  howpublished = {{Plenarprotokoll {wp}/{dok_nr}}},",
        f"  url = {{{pdf_url}}},",
        f"  note = {{{note}}}",
        "}",
    ]

    return "\n".join(lines)


def scan_all_protocols(term, start_year=2000):
    """
    Schritt 1: Scannt alle BT-Plenarprotokolle via plenarprotokoll-text.
    Gibt Liste der Protokolle zurück, die den Begriff enthalten.
    """
    print(f"🔍 Scanne alle BT-Protokolle ab {start_year} nach »{term}«...", file=sys.stderr)

    matching = []
    cursor = None
    checked = 0
    start_date = f"{start_year}-01-01"

    params = {
        "f.zuordnung": "BT",
        "f.datum.start": start_date,
        "format": "json",
        "apikey": API_KEY,
        "limit": 50,
    }

    while True:
        if cursor:
            params["cursor"] = cursor

        query = urllib.parse.urlencode(params)
        url = f"{BASE_URL}/plenarprotokoll-text?{query}"

        try:
            with urllib.request.urlopen(url, timeout=60) as resp:
                data = json.loads(resp.read().decode('utf-8'))
        except Exception as e:
            print(f"  ❌ API-Fehler: {e}", file=sys.stderr)
            break

        documents = data.get("documents", [])
        cursor = data.get("cursor")
        total = data.get("numFound", 0)

        if not documents:
            break

        checked += len(documents)
        print(f"  📄 {checked}/{total} Protokolle gescannt, {len(matching)} Treffer...", file=sys.stderr)

        for doc in documents:
            text = doc.get("text", "")
            if term.lower() in text.lower():
                fundstelle = doc.get("fundstelle", {})
                xml_url = fundstelle.get("xml_url")
                if xml_url:
                    matching.append({
                        "datum": doc.get("datum", ""),
                        "xml_url": xml_url,
                        "pdf_url": fundstelle.get("pdf_url", ""),
                        "wahlperiode": str(doc.get("wahlperiode", "?")),
                        "dokumentnummer": str(doc.get("dokumentnummer", "?")).split("/")[-1],
                    })

        if not cursor:
            break

    print(f"  ✅ Scan abgeschlossen: {len(matching)} Protokolle mit »{term}«", file=sys.stderr)
    return sorted(matching, key=lambda x: x["datum"])


def extract_quotes(term, matching_protocols):
    """
    Schritt 2: XML-Parsing nur für Treffer-Protokolle.
    Gibt alle Zitate zurück, dedupliziert und pro Jahr gecappt.
    """
    print(f"\n📖 Extrahiere Zitate aus {len(matching_protocols)} Protokollen...", file=sys.stderr)

    all_quotes = []
    seen = set()       # Deduplizierung: (nachname, datum)
    year_counts = {}   # Per-Jahr-Zähler

    for proto in matching_protocols:
        datum = proto["datum"]
        try:
            dt = datetime.strptime(datum, "%Y-%m-%d")
            jahr = dt.year
            monat = dt.month
            tag = dt.day
        except Exception:
            continue

        # Per-Jahr-Cap prüfen
        if year_counts.get(jahr, 0) >= MAX_PER_YEAR:
            continue

        results = parse_xml_for_term(proto["xml_url"], term)

        for r in results:
            nachname = r["nachname"]
            key = (nachname.lower(), datum)
            if key in seen:
                continue
            seen.add(key)

            citekey = generate_citekey(nachname, jahr, monat, tag)
            wp = proto["wahlperiode"]
            dok_nr = proto["dokumentnummer"]

            sprecher_info = r["rolle"] if r["rolle"] else r["fraktion"]

            all_quotes.append({
                "datum": datum,
                "jahr": jahr,
                "monat": monat,
                "tag": tag,
                "vorname": r["vorname"],
                "nachname": nachname,
                "fraktion": r["fraktion"],
                "rolle": r["rolle"],
                "sprecher_info": sprecher_info,
                "context": r["context"],
                "top_title": r["top_title"],
                "pages": r["pages"],
                "person_id": r.get("person_id", ""),
                "citekey": citekey,
                "wp": wp,
                "dok_nr": dok_nr,
                "pdf_url": proto["pdf_url"],
            })

            year_counts[jahr] = year_counts.get(jahr, 0) + 1

            if year_counts[jahr] >= MAX_PER_YEAR:
                break  # Nächstes Protokoll

    return sorted(all_quotes, key=lambda x: x["datum"])


def write_output(term, quotes):
    """Schreibt strukturierten Output für AI-Sichtung."""
    lines = []
    lines.append(f"# BUNDESTAG-Recherche: {term}")
    lines.append(f"**Durchsucht:** Alle BT-Plenarprotokolle")
    lines.append(f"**Treffer:** {len(quotes)} Zitate")
    lines.append(f"**Max. pro Jahr:** {MAX_PER_YEAR}")
    lines.append("")
    lines.append("---")
    lines.append("")

    current_year = None
    for i, q in enumerate(quotes, 1):
        if q["jahr"] != current_year:
            current_year = q["jahr"]
            lines.append(f"## {current_year}")
            lines.append("")

        sprecher = f"{q['vorname']} {q['nachname']}"
        if q["sprecher_info"]:
            sprecher += f" ({q['sprecher_info']})"

        lines.append(f"### Treffer {i}: {q['datum']}")
        lines.append(f"**Sprecher:** {sprecher}")
        lines.append(f"**Protokoll:** {q['wp']}/{q['dok_nr']}")
        if q["pages"]:
            lines.append(f"**Seiten:** {q['pages']}")
        lines.append(f"**PDF:** {q['pdf_url']}")
        lines.append("")
        lines.append(f"\u201e{q['context']}\u201c")
        lines.append("")
        lines.append(f"**Citekey:** `{q['citekey']}`")
        lines.append("")
        lines.append("```bibtex")
        lines.append(generate_bibtex(
            q["nachname"], q["vorname"], q["jahr"], q["monat"], q["tag"],
            q["wp"], q["dok_nr"], q["pdf_url"], q["citekey"], q["rolle"],
            q["top_title"], q["pages"], q.get("person_id", "")
        ))
        lines.append("```")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Alle BibTeX am Ende
    lines.append("## Alle BibTeX-Einträge")
    lines.append("")
    lines.append("```bibtex")
    for q in quotes:
        lines.append(generate_bibtex(
            q["nachname"], q["vorname"], q["jahr"], q["monat"], q["tag"],
            q["wp"], q["dok_nr"], q["pdf_url"], q["citekey"], q["rolle"],
            q["top_title"], q["pages"], q.get("person_id", "")
        ))
        lines.append("")
    lines.append("```")

    return "\n".join(lines)


if __name__ == "__main__":
    import os

    if len(sys.argv) < 2:
        print("Usage: python3 SCAN.py \"Begriff\" [Startjahr]")
        sys.exit(1)

    term = sys.argv[1]
    start_year = int(sys.argv[2]) if len(sys.argv) > 2 else 2000

    # Output-Datei
    script_dir = os.path.dirname(os.path.abspath(__file__))
    recherche_dir = os.path.join(script_dir, "Recherche", term)
    os.makedirs(recherche_dir, exist_ok=True)
    output_file = os.path.join(recherche_dir, f"DIP-{term}.md")

    print(f"🚀 BUNDESTAG-Recherche v4: »{term}« (ab {start_year})", file=sys.stderr)
    print(f"💾 Output: {output_file}", file=sys.stderr)
    print("", file=sys.stderr)

    # Schritt 1: Alle Protokolle scannen
    matching = scan_all_protocols(term, start_year)

    if not matching:
        print(f"⚠️  Keine Treffer für »{term}«", file=sys.stderr)
        sys.exit(0)

    # Schritt 2: Zitate extrahieren
    quotes = extract_quotes(term, matching)

    # Output schreiben
    output = write_output(term, quotes)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"\n✅ Fertig: {len(quotes)} Zitate → {output_file}", file=sys.stderr)
