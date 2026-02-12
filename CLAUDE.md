# WÖRTER - gpunkt.org Content

**Repository:** Content-Quelle für gpunkt.org (Reizwörterbuch)
**GitHub:** https://github.com/alemsabic/gpunkt-woerter (public)
**Site-Repo:** `/Users/alemsabic/Desktop/gpunkt.org`
**Ziel:** Politische Reizwörter dokumentieren — verifizierte Quellen, wissenschaftliche Mechanismus-Analyse.

## ⚠️ REPO-STRUKTUR

`wort-fabrik/` ist ein **eigenständiges privates Repository** innerhalb dieses Repos:
- **GitHub:** https://github.com/alemsabic/wort-fabrik (private)
- **Lokal:** `/Users/alemsabic/Desktop/MEMEX/WÖRTER/wort-fabrik/`
- In `.gitignore` von WÖRTER ausgeschlossen — **niemals** in gpunkt-woerter commiten!
- Eigene `git`-Befehle: immer erst `cd wort-fabrik/` dann commiten/pushen

## 🔥 NÄCHSTER SCHRITT

**Trigger:** *"Claude, vieux copain, what's on the plate"*

**DRAFT.md repariert** ✓ — 5 strukturelle Probleme behoben:

1. ✅ Belege-Beispiel im Template → Placeholder (keine Halluzinations-Einladung mehr)
2. ✅ KONTEXT-Material raus aus DRAFT-Chat → saubere Trennung Schreiben / Belege
3. ✅ "Anwendung" → "Perspektivenwechsel" durchgezogen (5 Stellen)
4. ✅ "Entlarvung" → "Aufdeckung" im Philosophie-Abschnitt
5. ⏳ Sozialtourismus-Priming → zweites Referenzbeispiel, wenn Gutmensch-Eintrag fertig

**Nächste Schritte:**
1. **DRAFT.md-Testlauf mit "Gutmensch":**
   - Neuen Claude-Chat öffnen
   - `wort-fabrik/DRAFT.md` einfügen, Begriff = `Gutmensch`
   - Phasen A → B → C → D → E sequenziell durchlaufen — nach jeder Phase stoppen, Zusammenfassung lesen, bestätigen
   - Outputs landen in: `Recherche/Gutmensch/PHASE-A-Lexikalisch.md`, `PHASE-B-Historisch.md`, `PHASE-C-Diskurs.md`, `PHASE-D-Mechanismen.md`
   - First Draft landet in: `Drafts/Gutmensch-draft.md`
   - **Dann kritisch prüfen:** Recherche-Dateien A–D — was ist gut, was fehlt, was ist falsch? Draft — stimmt die Struktur? Ist der Perspektivenwechsel überzeugend? Sind Belege sauber als Placeholder?
   - Erkenntnisse → DRAFT.md weiter verbessern
2. `to_zotero.bib` klären: Append-Logik, Format v5.2, Zotero-Import
3. Kompletten Lauf dokumentieren: HANDBUCH.md aktualisieren

---

---

## 🧠 SYSTEM-PRINZIP

**Quick Fix vs. Am System arbeiten:**
Wenn ein Output-Fehler auftritt, nicht die Output-Datei korrigieren — herausfinden, welche Instruktion in welchem Prompt-Dokument den Fehler *ermöglicht* hat, und das Dokument selbst fixen.

Konkretes Beispiel: `[X]` als Zahlen-Platzhalter und `[A]`/`[K]` als Literal-Labels in derselben Zeile — visuell identische Notation, zwei verschiedene Bedeutungen. KI wendet konsistent die falsche Regel an. Fix: unterschiedliche Notation (`N` für Zahlen, eckige Klammern nur für Literal-Labels).

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

*Letzte Aktualisierung: 2026-02-12*
