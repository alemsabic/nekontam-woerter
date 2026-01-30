# Claude Code Instructions - WÖRTER Repository (gpunkt.org Content)

## ⚠️ Project Overview

**Repository:** Content-Quelle für gpunkt.org (Reizwörterbuch)
**Site-Repo:** `/Users/alemsabic/Desktop/gpunkt.org`
**Sync:** Auto-sync via GitHub Actions → `gpunkt-site/content/`

**Ziel:** Politische Reizwörter mit verifizierten, zitierfähigen Quellen belegen.

---

## Current State (Status Quo)

### ✅ Was funktioniert:
- Markdown-Dateien mit Reizwörtern (z.B. `alternativlos.md`)
- Gemini-Recherche-Prompt für Zitate (`wort-fabrik/RECHERCHE-ZITATE.md`)
- Recherche-Ergebnisse (z.B. `wort-fabrik/Recherche/Recherche-Zitate-alternativlos.md`)
- Citations-Plugin aktiviert in gpunkt.org
- `bibliography.bib` existiert (1 Test-Eintrag)

### ❌ Was fehlt:
- **Keine BibTeX-Einträge** für die recherchierten Zitate
- **Inline-Zitate** statt pandoc-citations (`[@citekey]`)
- **Kein Verification-Workflow** (wie `verify_citations.py` in NOTIZEN)
- **Keine dreifache Quellen-Prüfung** (KRITISCH für Politiker-Zitate!)
- **Kein Zotero-Workflow** für Bibliography-Pflege

---

## Target State (Wie NOTIZEN)

### 📚 NOTIZEN als Referenz:
- `/Users/alemsabic/Desktop/MEMEX/NOTIZEN/`
- `zettel-fabrik/verify_citations.py` → Findet fehlende Citekeys
- `bibliography.bib` → Gepflegt via Zotero
- Alle Zitate: `[@autor_jahr]` Format
- Auto-Verification vor Commit

### 🎯 Ziel für WÖRTER:
Identischer Standard für wissenschaftlich fundierte Reizwort-Analyse.

---

## TODOs

### Phase 1: Gemini-Prompt erweitern ✅ TODO

**Datei:** `wort-fabrik/RECHERCHE-ZITATE.md`

**Ergänzungen:**
1. **BibTeX-Output zusätzlich zu Zitaten**
   - Gemini soll BEIDE Formate liefern:
     - Menschenlesbare Zitate (wie bisher)
     - BibTeX-Einträge für jeden Fund

2. **Triple-Verification Workflow**
   - KRITISCH: Jede Quelle muss 3x geprüft werden:
     1. Link öffnen → Zitat im Original finden
     2. Kontext prüfen → Ist das Zitat korrekt kontextualisiert?
     3. Metadaten prüfen → Datum, Name, Funktion korrekt?
   - Bei Unsicherheit → NICHT verwenden

3. **BibTeX-Format-Vorgaben**
   ```bibtex
   @misc{rottgen_2011,
     title = {Rede im Deutschen Bundestag zum Atomausstieg},
     author = {Röttgen, Norbert},
     year = {2011},
     month = {06},
     day = {30},
     howpublished = {Plenarprotokoll 17/117, Deutscher Bundestag},
     url = {https://dserver.bundestag.de/btp/17/17117.pdf},
     note = {Seite 13322}
   }
   ```

**Action:**
- [ ] Prompt ergänzen um BibTeX-Output-Sektion
- [ ] Triple-Verification-Checkliste hinzufügen
- [ ] BibTeX-Beispiele für verschiedene Quellentypen

---

### Phase 2: Bestehende Dateien konvertieren 🔴 TODO

**Dateien:**
- `alternativlos.md`
- `anatomke.md`
- `antifriz.md`
- `bagerke.md`
- `baklava.md`
- `Kopfkino.md`
- `Putinversteher.md`
- `Remigration.md`
- `Sozialtourismus.md`

**Konvertierung:**
1. **Inline-Text → Pandoc-Citations**
   - **Vorher:**
     ```markdown
     Norbert Röttgen (CDU, Umweltminister) Juni 2011 im Bundestag zum Atomausstieg nach Fukushima: »Wir halten den Ausstieg für alternativlos...«
     ```
   - **Nachher:**
     ```markdown
     Norbert Röttgen (CDU, Umweltminister) im Bundestag zum Atomausstieg [@rottgen_2011]: »Wir halten den Ausstieg für alternativlos...«
     ```

2. **BibTeX-Einträge erstellen**
   - Recherche-Dateien als Quelle nutzen
   - Für jedes Zitat: BibTeX-Eintrag in `bibliography.bib`

3. **Metadaten-Abgleich**
   - Namen, Funktionen, Daten gegen Recherche prüfen
   - Bei Abweichungen: Recherche-Datei als Ground Truth

**Action:**
- [ ] Template für Konvertierung erstellen
- [ ] Datei für Datei durchgehen (9 Dateien)
- [ ] bibliography.bib parallel aufbauen

---

### Phase 3: verify_citations.py adaptieren 🔴 TODO

**Referenz:** `/Users/alemsabic/Desktop/MEMEX/NOTIZEN/zettel-fabrik/verify_citations.py`

**Anpassungen für WÖRTER:**
1. **ZETTELKASTEN_DIR:**
   ```python
   ZETTELKASTEN_DIR = Path(__file__).parent.parent  # /MEMEX/WÖRTER/
   ```

2. **EXCLUDE_FILES:**
   ```python
   EXCLUDE_FILES = ["README.md", "index.md", "CLAUDE.md", "wort-fabrik/**"]
   ```

3. **Workflow:**
   - Findet fehlende `[@citekeys]` in .md Dateien
   - Vergleicht mit `bibliography.bib`
   - Generiert Stubs für Zotero-Import

**Action:**
- [ ] Skript nach `wort-fabrik/verify_citations.py` kopieren
- [ ] Pfade anpassen
- [ ] Testen mit bestehenden Dateien

---

### Phase 4: Zotero-Workflow etablieren 🔴 TODO

**Ziel:** Wissenschaftliche Bibliography-Pflege

**Workflow:**
1. **Gemini-Recherche** → BibTeX-Stubs
2. **Manuelle Triple-Verification** → Quellen prüfen
3. **Zotero-Import** → Metadaten vervollständigen
4. **Better BibTeX Export** → `bibliography.bib` aktualisieren
5. **verify_citations.py** → Fehler finden

**Zotero-Einstellungen:**
- Better BibTeX Plugin installieren
- Citation Key Formula: `[auth:lower]_[year]`
- Auto-Export: `bibliography.bib` → `/Users/alemsabic/Desktop/MEMEX/WÖRTER/`

**Action:**
- [ ] Zotero Collection "gpunkt.org Quellen" erstellen
- [ ] Better BibTeX Auto-Export konfigurieren
- [ ] Test-Import mit clark_chalmers_1998

---

### Phase 5: Recherche-Pipeline automatisieren 🟡 FUTURE

**Vision:** Neue Reizwörter schnell belegen

**Pipeline:**
1. Neues Wort → Gemini-Prompt
2. Gemini liefert: Zitate (markdown) + BibTeX
3. Triple-Verification (manuell!)
4. Zotero-Import
5. Markdown-Datei schreiben mit `[@citekeys]`
6. verify_citations.py → Check
7. Commit & Push

**Action:**
- [ ] Template für neue Wörter erstellen
- [ ] Checklist für Recherche
- [ ] (Optional) GitHub Action für auto-verify

---

## Workflows

### ⚡ Workflow 0: Automatisiert (recherche.sh) **← HAUPTWORKFLOW**

**Wann:** Neuen Begriff recherchieren + Draft erstellen

1. **Ein Befehl:**
   ```bash
   cd /Users/alemsabic/Desktop/MEMEX/WÖRTER
   ./wort-fabrik/recherche.sh "Remigration"
   ```

2. **Was passiert automatisch:**
   - ✅ Gemini recherchiert (Zitate + Mechanismus-Analyse)
   - ✅ Gemini schreibt First Draft (vollständiger Eintrag)
   - ✅ BibTeX extrahiert → `wort-fabrik/imports/to_zotero.bib`

3. **Outputs:**
   - `wort-fabrik/Recherche/Recherche-Remigration.md`
   - `wort-fabrik/Drafts/Draft-Remigration.md`
   - `wort-fabrik/imports/to_zotero.bib` (append)

4. **Triple-Verification (manuell):**
   - [ ] Links öffnen → Zitate im Original finden
   - [ ] Wort-für-Wort Vergleich
   - [ ] Kontext stimmt (nicht aus Zusammenhang gerissen)
   - [ ] Metadaten korrekt (Name, Funktion, Datum)
   - **Bei Unsicherheit:** Quelle aus `to_zotero.bib` löschen!

5. **Draft überarbeiten (mit Claude):**
   - Stil (Kriegsreporter-Haltung, Hauptsätze)
   - IPA Web-Safe prüfen (keine `i̯`, `u̯`, `t͡s`)
   - Mechanismus-Analyse plausibel?

6. **Zotero-Import:**
   - Zotero → File → Import → `wort-fabrik/imports/to_zotero.bib`
   - Metadaten vervollständigen (falls nötig)
   - Better BibTeX exportiert automatisch → `bibliography.bib`

7. **Finalisieren:**
   - Draft → Hauptordner verschieben: `Draft-Remigration.md` → `Remigration.md`
   - Cleanup: `rm wort-fabrik/imports/to_zotero.bib`
   - Verifizieren: `python3 wort-fabrik/verify_citations.py`

**Zeit:** ~5-10 Minuten (inkl. Triple-Verification + Überarbeitung)

---

### 🔍 Workflow 1: Manuell (für Spezialfälle)

**Wann:** Automatisierung funktioniert nicht / Spezielle Quellen

1. **Gemini-Recherche manuell:**
   ```bash
   # Prompt kopieren: wort-fabrik/RECHERCHE-PROMPT.md
   # Begriff einsetzen: [BEGRIFF HIER EINSETZEN]
   # Output manuell speichern
   ```

2. **Triple-Verification** (wie Workflow 0)

3. **BibTeX manuell:**
   - Aus Recherche extrahieren
   - In `wort-fabrik/imports/to_zotero.bib` einfügen

4. **Eintrag manuell schreiben:**
   - Template: `wort-fabrik/VORLAGE.md`
   - Mechanismus-Analyse: `wort-fabrik/WERKZEUGKASTEN.md`

5. **Zotero + Verifizieren** (wie Workflow 0)

---

### 📝 Workflow 2: Bestehende Datei konvertieren

1. **Recherche-Datei öffnen:**
   - Beispiel: `wort-fabrik/Recherche/Recherche-Zitate-alternativlos.md`

2. **Pro Zitat:**
   - BibTeX-Eintrag erstellen (Citekey: `autor_jahr`)
   - In bibliography.bib eintragen
   - Markdown-Datei anpassen: `[@autor_jahr]`

3. **Metadaten-Check:**
   - Gegen Recherche-Datei abgleichen
   - Bei Unsicherheit: Quelle erneut prüfen

4. **Verifizieren:**
   ```bash
   python3 wort-fabrik/verify_citations.py
   ```

---

## Critical Rules (⚠️ WICHTIG!)

### 1. Triple-Verification für Politiker-Zitate
**Warum:** Falsche Zuschreibung = Rufschädigung + Glaubwürdigkeitsverlust

**Checkliste:**
- [ ] Original-Quelle geöffnet (Link funktioniert)
- [ ] Zitat Wort-für-Wort im Original gefunden
- [ ] Kontext stimmt (nicht aus Zusammenhang gerissen)
- [ ] Metadaten korrekt (Name, Funktion, Datum, Anlass)

**Bei Unsicherheit:** Quelle NICHT verwenden!

---

### 2. BibTeX Citekey Standard
**Format:** `autor_jahr` (lowercase, Unterstrich)

**Beispiele:**
- ✅ `merkel_2010`
- ✅ `rottgen_2011`
- ✅ `habeck_2022`
- ❌ `Merkel2010`
- ❌ `merkel-2010`

**Konflikte (mehrere Zitate pro Autor/Jahr):**
- `merkel_2010a`, `merkel_2010b`, etc.

---

### 3. Bibliography.bib Pflege
- **NUR via Zotero** (keine manuellen Edits!)
- Better BibTeX Auto-Export aktivieren
- verify_citations.py vor jedem Commit

---

## Progress Tracker

### Sprint 1: Foundation ✅
- [x] Citations-Plugin aktiviert in gpunkt.org
- [x] bibliography.bib existiert
- [x] CSL-Ordner analysiert (nicht notwendig)
- [x] CLAUDE.md erstellt

### Sprint 2: Tooling ✅ COMPLETED (2026-01-30)
- [x] Gemini-Prompt erweitert (BibTeX-Output)
  - Triple-Verification Workflow (3 Prüfungen)
  - 9-Punkte Verification-Checkliste
  - 6 BibTeX-Templates für verschiedene Quellentypen
  - AI-Halluzinations-Warnungen
  - Citekey-Standard dokumentiert
- [x] verify_citations.py adaptiert
  - Skript von NOTIZEN nach wort-fabrik/ kopiert
  - Pfade angepasst (wort-fabrik/imports/)
  - WÖRTER-spezifische Warnungen (Triple-Verification)
  - Getestet: Erkennt fehlende [@citekeys], generiert to_zotero.bib
- [x] Imports-Struktur erstellt
  - wort-fabrik/imports/ Ordner
  - README.md mit Workflow-Dokumentation
  - .gitignore für to_zotero.bib
- [x] Gemini-Prompt Iteration basierend auf Feedback
  - Qualitätsmedien erlaubt (FAZ, SZ, ARD, ZDF mit Bedingungen)
  - 3-4 Zitate statt 5-7 (Qualität > Quantität)
  - Subtextueller Kontext (Waffeneinsatz dokumentieren)
  - Behutsame Glättung erlaubt (Füllwörter mit [...])
- [x] PROMPT-GEMINI.md erstellt
  - Copy-paste-ready (~120 Zeilen)
  - Separate von Dokumentation (RECHERCHE-ZITATE-V3.md)
  - Getestet mit "Passdeutsche"

### Sprint 3: Mechanismus-Analyse verbessern 🔴 TODO

**Problem:** Aktuelle Kategorien (Euphemismus, Dysphemismus, etc.) sind zu simpel für komplexe Manipulations-Mechanismen.

**Ziel:** Besserer Werkzeugkasten zur Analyse politischer Kampfbegriffe.

#### Phase 1: Kategorien-System überarbeiten
- [ ] **Analyse bestehender Kategorien** (LEXIKON-STANDARD-POLITIK.md)
  - Welche Kategorien funktionieren?
  - Welche sind zu vage?
  - Welche fehlen?

- [ ] **Neue/bessere Kategorien entwickeln**
  - Ethnisierung (Rechtsstatus → Blut/Abstammung)
  - Naturalisierung (Politik → Naturgesetz)
  - Temporalisierung (Gegenwart → Zukunftsbedrohung)
  - Quantifizierung (Einzelfall → Massenphänomen)
  - Inversionen (gut → schlecht)

- [ ] **Kategorien-Taxonomie erstellen**
  - Hierarchie (Ober-/Unterkategorien)
  - Kombinierbar? (Begriff kann mehrere Kategorien haben)
  - Klare Definitionen + Beispiele

#### Phase 2: RECHERCHE-MECHANISMUS.md verbessern
- [ ] **Prompt schärfen**
  - Bessere Fragen zu Manipulations-Mechanismen
  - Strukturierte Analyse-Checkliste
  - Output-Format präziser

- [ ] **Werkzeugkasten einbauen**
  - Welche Mechanismen soll Perplexity erkennen?
  - Checkliste für AI: "Prüfe auf..."
  - Beispiele für gute vs. schlechte Analysen

#### Phase 3: Prompts vereinheitlichen? 🤔 ERWÄGEN
- [ ] **Bewertung: 2 Prompts vs. 1 kombinierter Prompt**

  **Status Quo (2 Prompts):**
  - PROMPT-GEMINI.md → Zitate recherchieren
  - RECHERCHE-MECHANISMUS.md → Mechanismen analysieren
  - Vorteil: Spezialisiert, fokussiert
  - Nachteil: Doppelte Arbeit, Mechanismen oft oberflächlich

  **Alternative (1 kombinierter Prompt):**
  - Ein Prompt: Zitate + Mechanismus-Analyse in einem
  - AI untersucht Zitate direkt auf Manipulations-Mechanismen
  - Vorteil: Effizienter, tiefere Analyse
  - Nachteil: Längerer Prompt, AI könnte überfordert sein

  **Entscheidung:** Erst Werkzeugkasten fertig, dann testen!

#### Phase 4: LEXIKON-STANDARD-POLITIK.md aktualisieren
- [ ] **Kategorien-Sektion erweitern**
  - Neue Kategorien einbauen
  - Bessere Beispiele
  - Klare Abgrenzungen

- [ ] **Mechanismus-Sektion verbessern**
  - Detailliertere Anleitung
  - Mehr Beispiele (gut vs. schlecht)
  - Werkzeugkasten-Referenz

---

### Sprint 4: Migration (PAUSED bis Sprint 3 fertig)
- [ ] 9 bestehende Dateien konvertiert
- [ ] bibliography.bib vollständig
- [ ] Alle Quellen triple-verified
- [ ] Zotero-Workflow etabliert

### Sprint 5: Automation 🟡 FUTURE
- [ ] Template für neue Wörter
- [ ] GitHub Action für auto-verify
- [ ] Recherche-Pipeline dokumentiert

---

## Session Summary (2026-01-30)

**Was erreicht:**
- ✅ Citations-Plugin für gpunkt.org aktiviert
- ✅ verify_citations.py für WÖRTER adaptiert
- ✅ PROMPT-GEMINI.md (copy-paste-ready, ~120 Zeilen)
- ✅ Qualitätsmedien-Regelwerk (FAZ, SZ, ARD mit Bedingungen)
- ✅ Werkzeugkasten-Grundlage (3-4 Zitate, Subtextueller Kontext)

**Erkenntnisse:**
- Gemini ignoriert "KEINE Sekundärquellen"-Regel teilweise
- Qualitätsmedien MÜSSEN erlaubt sein (FAZ, ARD haben viel zu verlieren)
- 5-7 Zitate führen zu Füllmaterial → 3-4 stärkste Treffer besser
- Triple-Verification bleibt PFLICHT (auch bei FAZ!)

**Nächste Session:**
1. Mechanismus-Kategorien überarbeiten
2. RECHERCHE-MECHANISMUS.md verbessern
3. Erwägen: 2 Prompts → 1 kombinierter Prompt
4. Werkzeugkasten für Manipulations-Analyse erstellen

---

## Notes

**Unterschied zu NOTIZEN:**
- NOTIZEN: Akademische Quellen (Papers, Bücher)
- WÖRTER: Primärquellen (Politiker-Zitate, Bundestagsreden)
- → WÖRTER braucht strengere Verification (Triple-Check!)

**Gemini vs. ChatGPT:**
- Gemini: Besser für strukturierte Extraktion (Bundestagsprotokolle)
- Triple-Verification bleibt IMMER manuell (AI-Halluzination!)

---

*Erstellt: 2026-01-30*
*Letzte Aktualisierung: 2026-01-30*
