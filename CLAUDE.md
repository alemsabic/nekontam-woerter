# WÖRTER - gpunkt.org Content

**Repository:** Content-Quelle für gpunkt.org (Reizwörterbuch)
**Site-Repo:** `/Users/alemsabic/Desktop/gpunkt.org`
**Ziel:** Politische Reizwörter dokumentieren — verifizierte Quellen, wissenschaftliche Mechanismus-Analyse.

## 🔥 NÄCHSTER SCHRITT

**Trigger:** *"Claude, vieux copain, what's on the plate"*

**SICHTEN-Workflow fertigstellen** — der komplette Pipeline-Schritt SCAN → SICHTEN → DRAFT → Zotero muss lückenlos funktionieren:

1. **SICHTEN.md testen:** `DIP-Gutmensch.md` + `SICHTEN.md` in Claude-Chat → `KONTEXT-Gutmensch.md` erzeugen → Format kritisch prüfen, bis es perfekt ist
2. **DRAFT.md-Anschluss prüfen:** KONTEXT-Datei direkt in DRAFT.md einspeisen — passt der Workflow? Müssen Phasen A–E angepasst werden?
3. **`to_zotero.bib` klären:** Append-Logik (mehrere Begriffe akkumulieren), Format stimmt mit v5.2 überein, fertig zum Zotero-Import
4. **Kompletten Lauf dokumentieren:** Wenn alles passt, HANDBUCH.md aktualisieren

---

## 📋 WORKFLOW

```bash
python3 wort-fabrik/SCAN.py "Begriff"   # ~10 min, läuft im Hintergrund
```
Dann: `SICHTEN.md` + DIP-Datei → `KONTEXT-[Begriff].md` → `DRAFT.md` (Phasen A–E) → `EDIT.md` (optional) → Zotero → `VERIFY.py`

**Vollständige Dokumentation:** `wort-fabrik/HANDBUCH.md`

---

## ⚠️ CRITICAL RULES

### BibTeX Format

**Citekey:** `autor_jahr_monat_tag` (lowercase, zero-padded)
- ✅ `springer_2018_06_28`, `schaeuble_2014_04_08`
- Kollisionssicher: ein Politiker hält pro Sitzungstag eine Rede

**Zotero Better BibTeX** (Einstellungen → Better BibTeX → Citation key formula):
```
auth.lower + "_" + date('%Y_%m_%d')
```

**Pflichtfelder:**

| Feld | Inhalt |
|---|---|
| `title` | TOP-Titel aus XML (Fallback: `Rede im Deutschen Bundestag (Plenarprotokoll XX/YY)`) |
| `address` | parlamentsspezifisch (siehe Tabelle unten) |
| `organization` | parlamentsspezifisch (siehe Tabelle unten) |
| `number` | `18/73` (Wahlperiode/Dokumentnummer) |
| `pages` | `7012A--7014C` |
| `note` | `Plenarprotokoll XX/YY` |

**Parlamente:**
| Parlament | `address` | `organization` |
|---|---|---|
| Bundestag | `Berlin` | `Deutscher Bundestag` |
| Bundesrat | `Berlin` | `Bundesrat` |
| Bayerischer Landtag | `München` | `Bayerischer Landtag` |
| Landtag NRW | `Düsseldorf` | `Landtag Nordrhein-Westfalen` |
| Sächsischer Landtag | `Dresden` | `Sächsischer Landtag` |
| Europaparlament | `Straßburg` | `Europäisches Parlament` |

In SCAN.py: `address`/`organization` sind Parameter in `generate_bibtex()`, Default `Berlin`/`Deutscher Bundestag`.

### Keine Sekundärquellen
- ✅ Bundestag-Protokolle, Original-Videos, Qualitätsmedien mit wörtlicher Rede
- ❌ Indirekte Rede, "X berichtet, dass Y sagte..."

### Belege im Draft
- KI füllt Belege NICHT aus — kommen aus KONTEXT-MATERIAL, manuell per Zotero

### Draft-Prinzip (3-DRAFT-THIS.md v2.0)
- **First Draft mit Speck:** Logik + vollständige Gedankengänge, keine sprachliche Brillanz (kommt in EDIT)
- Phase-Outputs werden in Dateien geschrieben (`PHASE-A-Lexikalisch.md` etc.) — STOPP nach jeder Phase
- Sektion heißt **Perspektivenwechsel**, nicht "Anwendung" — erster Satz immer: `**Sicht des Sprechers:**`
- Keine Anklage-Sprache ("entlarvt", "versteckt") — Advocatus Diaboli

---

## 📁 DATEIEN

**Pipeline:**
- `wort-fabrik/SCAN.py` — Bundestag-Scan (v4)
- `wort-fabrik/DRAFT.md` — Recherche + Draft (Phasen A–E)
- `wort-fabrik/EDIT.md` — Polishing
- `wort-fabrik/VERIFY.py` — Citekey-Prüfung

**Referenz:**
- `wort-fabrik/CITING_STANDARDS.md` — BibTeX-Goldstandard mit Beispiel
- `wort-fabrik/Queue.md` — 100 Begriffe in der Pipeline

**Ordner:**
- `wort-fabrik/Recherche/[Begriff]/` — DIP-Outputs + Phase-Dateien
- `wort-fabrik/Drafts/` — Entwürfe
- `wort-fabrik/imports/to_zotero.bib` — BibTeX-Sammler (temporär)

---

## 📚 ZUSÄTZLICHE QUELLEN (SPÄTER)

**Landtage:** [Bayern](https://www.bayern.landtag.de/parlamentsdokumente/) · [NRW](https://www.landtag.nrw.de/portal/WWW/dokumentenarchiv/) · [Sachsen](https://edas.landtag.sachsen.de/)
**Europaparlament:** [Plenarprotokolle](https://www.europarl.europa.eu/plenary/de/debates-video.html)
**Bundesrat:** [Plenarprotokolle](https://www.bundesrat.de/DE/plenum/plenum-kompakt/plenum-kompakt-node.html)

---

*Letzte Aktualisierung: 2026-02-11*
