# RECHERCHE-PROMPT: Zitate + Mechanismus-Analyse

**An:** Gemini (oder andere Research-AI)
**Projekt:** gpunkt.org - Dokumentation politischer Kampfbegriffe
**Ziel:** 3-4 starke Zitate finden + Mechanismus-Analyse der manipulativen Strategien

---

## KONTEXT

Ich recherchiere für ein dokumentarisches Wörterbuch über politische Kampfbegriffe und diskriminierende Vulgärsprache.

**Begriff:** "[BEGRIFF HIER EINSETZEN]"

**Deine Rolle:**
Du bist ein akribischer Rechercheur. Wir suchen die **3-4 stärksten Zitate**, die zeigen, wie dieser Begriff als Machtinstrument eingesetzt wird (Debatten beenden, ausgrenzen, kriminalisieren, entmenschlichen). Zusätzlich analysierst du die manipulativen Mechanismen.

---

## TEIL 1: QUELLEN-ANFORDERUNGEN

### ✅ ERLAUBT:

**Primärquellen (höchste Priorität):**
- Bundestag/Landtag-Protokolle (mit Seitenzahl)
- Original-Videos (mit Zeitstempel: ab MM:SS)
- Parteitagsprotokolle
- Offizielle Pressemitteilungen

**Qualitätsmedien (mit Bedingungen):**
- FAZ, SZ, Spiegel, Zeit, ARD, ZDF, Deutschlandfunk, Tagesschau.de
- **BEDINGUNG:** Zitat MUSS in **»Anführungszeichen«** stehen (wörtliche Rede)
- **Bevorzugt:** Video/Audio mit Zeitstempel (verifizierbar)
- **Akzeptabel:** Schriftliches Interview mit direktem Zitat

---

### ❌ VERBOTEN:

- Sekundär-Sekundärquellen ("Zeitung A über Zeitung B")
- Kritiker-Zitate (wir suchen Täter, nicht Kritiker!)
- Indirekte Rede ("Er sagte, dass...")
- Blogs, Social Media ohne Original-Link
- Tagesschau-Bericht OHNE Link zum Original-Video

---

## TEIL 2: AUSWAHLKRITERIEN (die 3-4 stärksten)

✅ **Waffeneinsatz sichtbar:**
- Debatte wird beendet ("alternativlos")
- Macht wird ausgeübt (Kriminalisierung: "wer betrügt, der fliegt")
- Kritik wird delegitimiert (Inversion: "Meinungsdiktatur")
- Menschen werden entmenschlicht ("Flut", "Tourismus")

✅ **Historisch relevant:**
- Wendepunkt in der Debatte
- Skandal/öffentliche Empörung
- Unwort des Jahres

✅ **Prominent:**
- Minister/Parteispitzen > Hinterbänkler
- Öffentliche Bühne (Bundestag, TV-Interview) > Twitter

✅ **Prägnant:**
- Kurz, eingängig, provokant
- Zeigt Mechanismus klar (nicht vage)

---

❌ **Vermeide Füllmaterial:**
- Technische Verwendung ("Die Umgehungsstraße ist alternativlos")
- Banale Kontexte (Lokalpolitik ohne Relevanz)

**Behutsame Glättung erlaubt:**
- Füllwörter ("äh, also, ja") mit `[...]` streichen
- Kernaussage bleibt identisch

---

## TEIL 3: MECHANISMUS-ANALYSE

Analysiere für jedes Zitat, **welche manipulativen Mechanismen** am Werk sind.

**Werkzeugkasten (12 Mechanismen):**

**Politische Kampfbegriffe:**
1. **Ethnisierung** - Problem → ethnische/kulturelle Zugehörigkeit
2. **Naturalisierung** - Politik → Naturgesetz ("alternativlos")
3. **Quantifizierung** - Menschen → Masse/Zahlen ("Flut")
4. **Temporalisierung** - Gegenwart → Apokalypse ("Volkstod")
5. **Inversion** - Täter ↔ Opfer ("Meinungsdiktatur")
6. **Entpolitisierung** - Konflikt → Technik/Sachzwang
7. **Militarisierung** - Zivil → Krieg ("Klimaterroristen")
8. **Euphemismus** - Grausam → harmlos ("Remigration")

**Diskriminierende Vulgärsprache:**
9. **Kriminalisierung** - Legal → Verbrechen
10. **Infantilisierung** - Erwachsen → Kind ("Nasenpimmel")
11. **Sexualisierung** - Person → Sexualakt ("Schwanzlutscher")
12. **Entmenschlichung** - Mensch → Objekt/Tier/Fehler ("Fickfehler")

**Graduell bewerten:**
- **●** (stark/dominant) - Mechanismus ist zentral
- **◐** (teilweise) - Mechanismus ist erkennbar, aber nicht dominant
- **○** (nicht vorhanden) - Mechanismus wirkt nicht

**Vollständige Beschreibungen:** Siehe [WERKZEUGKASTEN.md](WERKZEUGKASTEN.md)

---

## TEIL 4: OUTPUT-FORMAT

Liefere für jeden Treffer:

---

**Zitat [Nr]: [Name] ([Partei], [Jahr])**

**Quelle:** [Name, Funktion, Medium/Kontext, Datum (TT.MM.JJJJ)]

**Link:** [Vollständige URL]

**Der subtextuelle Kontext:** [2-3 Sätze: Wie wurde der Begriff als Waffe eingesetzt? Debatte beendet? Macht ausgeübt? Kritik delegitimiert? Menschen entmenschlicht?]

**Mechanismus-Analyse:**
- **● [Mechanismus 1] (dominant)** - [Kurze Begründung, max. 5 Wörter]
- **● [Mechanismus 2]** - [Begründung]
- **◐ [Mechanismus 3] (teilweise)** - [Begründung]
- **○ [Mechanismus 4]** - nicht vorhanden

**Zitat:** »[Vollständiger Satz - behutsam geglättet mit [...] wenn nötig]«

**Citekey:** `nachname_jahr`

**Verification-Status:** [Anführungszeichen vorhanden? / Protokoll-Wortlaut? / Video-Zeitstempel?]

---

[3-4 Zitate in diesem Format]

---

**Hinweis zur Verifizierbarkeit:**
[Falls Unsicherheiten bestehen, hier dokumentieren]

---

## TEIL 5: BIBTEX-EINTRÄGE (für bibliography.bib)

Liefere für JEDES Zitat einen passenden BibTeX-Eintrag:

---

### Bundestagsrede:
```bibtex
@misc{nachname_jahr,
  title = {Rede im Deutschen Bundestag zu [Thema]},
  author = {Nachname, Vorname},
  year = {JJJJ},
  month = {MM},
  day = {TT},
  howpublished = {Plenarprotokoll XX/YYY, Deutscher Bundestag},
  url = {https://dserver.bundestag.de/btp/XX/XXYYYY.pdf},
  note = {Seite XXXX}
}
```

---

### Zeitungsinterview:
```bibtex
@article{nachname_jahr,
  title = {Artikel-Titel},
  author = {Nachname, Vorname},
  year = {JJJJ},
  month = {MM},
  day = {TT},
  journal = {Frankfurter Allgemeine Zeitung},
  url = {https://www.faz.net/...},
  note = {Interview, wörtliche Rede}
}
```

---

### Video (ARD/ZDF):
```bibtex
@misc{nachname_jahr,
  title = {Interview/Rede in [Sendung/Anlass]},
  author = {Nachname, Vorname},
  year = {JJJJ},
  month = {MM},
  day = {TT},
  howpublished = {ARD/ZDF},
  url = {https://www.ardmediathek.de/...},
  note = {Zeitstempel: ab MM:SS}
}
```

---

### YouTube (offizieller Kanal):
```bibtex
@misc{nachname_jahr,
  title = {Video-Titel},
  author = {Nachname, Vorname},
  year = {JJJJ},
  month = {MM},
  day = {TT},
  howpublished = {YouTube},
  url = {https://www.youtube.com/watch?v=...},
  note = {Offizieller Kanal, Zeitstempel: ab MM:SS}
}
```

---

### Pressemitteilung:
```bibtex
@misc{nachname_jahr,
  title = {Titel der Pressemitteilung},
  author = {Nachname, Vorname},
  year = {JJJJ},
  month = {MM},
  day = {TT},
  howpublished = {Pressemitteilung [Partei/Organisation]},
  url = {https://...},
  note = {Offizielle Website}
}
```

---

### Parteitag:
```bibtex
@misc{nachname_jahr,
  title = {Rede auf dem [Partei]-Parteitag},
  author = {Nachname, Vorname},
  year = {JJJJ},
  month = {MM},
  day = {TT},
  howpublished = {Parteitag [Stadt]},
  url = {https://...},
  note = {Video/Protokoll}
}
```

---

**WICHTIG:**
- **Author = der Sprecher** (NICHT der Journalist!)
- **Citekeys:** `nachname_jahr` (lowercase, z.B. `merkel_2010`)
- Bei mehreren Zitaten pro Person/Jahr: `nachname_jahr_a`, `nachname_jahr_b`
- Citekeys in Zitaten MÜSSEN EXAKT mit BibTeX übereinstimmen

---

## TEIL 6: TRIPLE-VERIFICATION (KRITISCH!)

**PFLICHT bei Politiker-Zitaten:**

Für JEDES Zitat diese 3 Prüfungen durchführen:

### ✓ Prüfung 1: Original finden
- Link öffnen
- Zitat Wort-für-Wort im Original suchen
- **Wenn nicht gefunden:** Quelle NICHT verwenden!

### ✓ Prüfung 2: Kontext prüfen
- Ist das Zitat korrekt kontextualisiert?
- Wird es aus dem Zusammenhang gerissen?
- **Bei Unsicherheit:** Quelle NICHT verwenden!

### ✓ Prüfung 3: Metadaten prüfen
- Name korrekt? (Vorname, Nachname)
- Funktion korrekt? (Minister, Parteivorsitzender)
- Datum korrekt? (TT.MM.JJJJ)
- **Bei Abweichung:** Korrigieren oder Quelle NICHT verwenden!

**Bei JEGLICHEM Zweifel:** Quelle NICHT verwenden!

**Lieber 2 perfekte Zitate als 4 unsichere.**

---

## TEIL 7: CHEAT-SHEET

### ✅ PERFEKT (Goldstandard):

- Bundestag-Protokoll mit Seitenzahl:
  - `https://dserver.bundestag.de/btp/17/17042.pdf` (S. 4160)
  - Wortlaut garantiert, öffentlich zugänglich, dauerhaft verfügbar

- ARD-Video mit Zeitstempel:
  - `https://www.ardmediathek.de/video/...` (ab 12:30)
  - Sicht- und hörbar, verifizierbar, öffentlich-rechtlich

- FAZ-Interview mit »Zitat« in Anführungszeichen:
  - Artikel zeigt wörtliche Rede in »Guillemets« oder "Anführungszeichen"
  - Journalist bürgt für Korrektheit

---

### ❌ VERBOTEN (niemals verwenden):

- "Correctiv berichtet, dass X sagte..."
  - Sekundär-Sekundärquelle (zwei Instanzen dazwischen)

- Tagesschau-Bericht OHNE Link zum Original-Video
  - Paraphrase, keine wörtliche Rede

- Social Media Screenshot ohne Verifikation
  - Kann gefälscht sein, kein Kontext

- Blog-Beitrag über Politiker-Aussage
  - Keine journalistische Verantwortung

---

## QUALITÄTSKRITERIEN

Dein Output muss erfüllen:

✅ **3-4 Zitate** (Qualität > Quantität)
✅ **Wörtliche Rede** (Anführungszeichen/Protokoll/Video)
✅ **Subtextueller Kontext** (Waffeneinsatz dokumentiert)
✅ **Mechanismus-Analyse** (3-6 Mechanismen, graduell ●◐○)
✅ **Chronologisch sortiert** (früheste → neueste)
✅ **BibTeX vollständig** (author, year, url, note)
✅ **Citekeys konsistent** (nachname_jahr, lowercase)
✅ **Triple-verified** (3 Prüfungen bestanden)

---

## ⚠️ WARNUNGEN

### Warnung 1: AI-Halluzination
**Problem:** Sprachmodelle erfinden manchmal Zitate oder Quellen.

**Schutz:**
- IMMER Link angeben (zum Prüfen)
- IMMER Verification-Status dokumentieren
- Bei Unsicherheit: Quelle NICHT verwenden

---

### Warnung 2: Rufschädigung
**Problem:** Falsche Zuschreibung = rechtliche Konsequenzen + Glaubwürdigkeitsverlust

**Schutz:**
- Triple-Verification (3 Prüfungen)
- Nur Primärquellen oder verifizierte Qualitätsmedien
- Kontext korrekt wiedergeben

---

### Warnung 3: Sekundärquellen
**Problem:** "Correctiv schreibt, dass Sellner sagte..." = zu viele Instanzen

**Schutz:**
- Nur Original-Quellen (Politiker selbst)
- Keine Berichte über Berichte

---

**Bei JEGLICHEM Zweifel:** Quelle NICHT verwenden!

**Lieber 2 perfekte Zitate als 4 unsichere.**

---

## STARTBEFEHL

**Starte jetzt die Recherche für "[BEGRIFF HIER EINSETZEN]".**

Liefere:
1. 3-4 starke Zitate (mit Kontext, Link, Mechanismus-Analyse)
2. BibTeX-Einträge für jedes Zitat
3. Hinweis zur Verifizierbarkeit (falls Unsicherheiten bestehen)

**Denk daran:**
- Triple-Verification (3 Prüfungen pro Zitat)
- Mechanismus-Analyse (graduell ●◐○)
- Subtextueller Kontext (Waffeneinsatz zeigen)
- BibTeX vollständig (author = Sprecher, nicht Journalist)

**Bei Unsicherheit:** Lieber weniger Zitate, dafür perfekt.
