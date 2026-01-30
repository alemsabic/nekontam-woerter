# Imports Directory

**Zweck:** Temporäre BibTeX-Stubs für Zotero-Import

## Workflow

1. **verify_citations.py findet fehlende Citations**
   ```bash
   cd /Users/alemsabic/Desktop/MEMEX/WÖRTER
   python3 wort-fabrik/verify_citations.py
   ```

2. **Stubs generieren**
   ```bash
   python3 wort-fabrik/verify_citations.py --fix
   ```
   → Erstellt `to_zotero.bib` mit Stubs für fehlende Citekeys

3. **Zotero-Import**
   - Zotero öffnen
   - File → Import → `to_zotero.bib`
   - Stubs erscheinen in "Unfiled Items"

4. **Metadaten vervollständigen**
   - **WICHTIG:** Recherche-Dateien nutzen (`wort-fabrik/Recherche/`)
   - Magic Wand (Zotero) für automatische Metadaten-Suche
   - Manuell korrigieren/ergänzen

5. **⚠️ TRIPLE-VERIFICATION** (PFLICHT!)
   - [ ] Link öffnen → Zitat im Original finden
   - [ ] Wort-für-Wort Vergleich
   - [ ] Metadaten korrekt (Name, Datum, Funktion)
   - Siehe: `RECHERCHE-ZITATE.md`

6. **Better BibTeX Export**
   - Collection auswählen → Rechtsklick
   - Export Collection → Format: "Better BibTeX"
   - Datei: `bibliography.bib` (überschreiben)

7. **Cleanup**
   ```bash
   rm wort-fabrik/imports/to_zotero.bib
   ```

---

## Dateien

- `to_zotero.bib` - Temporäre Import-Datei (wird von Skript generiert)
- `.gitignore` - Verhindert versehentlichen Commit von to_zotero.bib

---

**KRITISCH:** Stubs sind NUR Platzhalter! Ohne Triple-Verification sind sie nutzlos/gefährlich.
