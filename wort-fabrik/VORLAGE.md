# VORLAGE: Wörterbuch-Einträge

**Projekt:** gpunkt.org (Reizwörterbuch)
**Version:** 2.0 (30.01.2026)
**Umfang:** Politische Kampfbegriffe + Diskriminierende Vulgärsprache

---

## 1. TEMPLATE

```markdown
---
title: Sozialtourismus
language: de
cssclasses: dictionary-entry
tags:
  - Kampfbegriff
  - Inversion
  - Kriminalisierung
---

# Sozialtourismus

## [zoˈtsiaːltuˌʁɪsmʊs] · DER · politisch, ab 2013 · Dysphemismus

---

Kampfbegriff für Migration. Suggeriert, Menschen fliehen zum Vergnügen und besuchen Sozialsysteme wie Urlaubsziele. Verschleiert Fluchtgründe (Armut, Krieg, Diskriminierung). Kriminalisiert rechtmäßige EU-Freizügigkeit als Betrug.

**Mechanismus:** "Sozial-" (Sozialsystem als Ziel) + "Tourismus" (Vergnügungsreise) = existenzielle Not wird freiwilliger Konsum.

**Geprägt:** CSU/CDU 2013 (Friedrich, Seehofer, Dobrindt) im Kontext der EU-Osterweiterung. Erneut 2022: Merz (ukrainische Geflüchtete).

**Mechanismus-Analyse:**
- ● Inversion (dominant) - Not wird zu Luxus
- ● Kriminalisierung - Recht wird zu Betrug
- ● Ethnisierung - Ziel: Osteuropäer/Roma
- ● Euphemismus - "Tourismus" klingt harmlos
- ○ Quantifizierung - teilweise ("Massenmigration")

**Beispiel:** Hans-Peter Friedrich (CSU, Bundesinnenminister) im Spiegel-Interview März 2013 [@friedrich_2013]: »Wer aber nur kommt, um Sozialleistungen zu kassieren, der missbraucht das Freizügigkeitsrecht. Diesen ==Sozialtourismus== müssen wir unterbinden.« ● Horst Seehofer (CSU) bei der Kreuth-Klausur Januar 2013 [@seehofer_2013]: »Wir werden uns gegen Zuwanderung in die deutschen Sozialsysteme wehren – bis zur letzten Patrone. [...] Es gibt keinen ==Sozialtourismus== in die deutschen Sozialsysteme.«
```

---

## 2. KOMPONENTEN IM DETAIL

### 2.1 Frontmatter

```yaml
---
title: Sozialtourismus
language: de
cssclasses: dictionary-entry
tags:
  - Kampfbegriff
  - Inversion
  - Kriminalisierung
---
```

**Tags:**
- **"Kampfbegriff"** - PFLICHT bei politischen Begriffen
- **Mechanismen** - 1-3 dominante Mechanismen (aus Werkzeugkasten)
- **Zusätzlich** - "Vulgärsprache", "Jugendsprache", "Unwort" (optional)

---

### 2.2 Headword + Metadaten

```markdown
# Sozialtourismus

## [zoˈtsiaːltuˌʁɪsmʊs] · DER · politisch, ab 2013 · Dysphemismus

---
```

**Format:** H2 mit Middot `·` als Trenner

**Phonetik (IPA Web-Safe):**
- Betonung: `ˈ` vor betonter Silbe
- Lange Vokale: `ː` (z.B. `oː`)
- **WICHTIG:** Keine kombinierenden Diakritika! (siehe Abschnitt 3)

**Genus:** DER/DIE/DAS oder "Adjektiv" (ausgeschrieben)

**Zeitangabe:**
- **Politisch:** `politisch, ab JAHR`
- **Vulgär:** `umgangssprachlich, 20./21. Jahrhundert`

**Kategorie:**
- Dysphemismus (abwertend)
- Euphemismus (beschönigend)
- Kampfbegriff (politisch)

**HR-Element:** `---` nach Metadaten (PFLICHT!)

---

### 2.3 Definition

**Struktur (3-4 Sätze):**
1. Was ist es? (Kampfbegriff für X / Vulgärer Begriff für Y)
2. Wirkung (suggeriert, verschleiert, kriminalisiert)
3. Funktion (warum wird es benutzt?)

**Stil:**
- Hauptsätze (kurz, prägnant)
- Verben der Manipulation: "tarnt", "verschleiert", "suggeriert", "kriminalisiert", "entmenschlicht"
- KEINE Superlative, KEINE Emotionen ("zynisch", "perfide" → raus!)
- Kriegsreporter-Haltung: zeigen, nicht kommentieren

---

### 2.4 Mechanismus (PFLICHT)

```markdown
**Mechanismus:** "Sozial-" (Sozialsystem als Ziel) + "Tourismus" (Vergnügungsreise) = existenzielle Not wird freiwilliger Konsum.
```

**Format:**
- `**Mechanismus:**` (fett)
- Wortbestandteile in Anführungszeichen: `"Sozial-"`
- Bedeutung in Klammern: `(Sozialsystem als Ziel)`
- Plus-Zeichen zwischen Teilen: `+`
- Gleich-Zeichen vor Wirkung: `=`
- Wirkung: ein prägnanter Satz

**Länge:** Max. 2 Sätze

---

### 2.5 Geprägt (bei politischen Begriffen)

```markdown
**Geprägt:** CSU/CDU 2013 (Friedrich, Seehofer, Dobrindt) im Kontext der EU-Osterweiterung. Erneut 2022: Merz.
```

**Format:**
- `**Geprägt:**` (fett)
- Wer: Name oder Partei (Jahr)
- Kontext: ein Halbsatz (Warum entstand der Begriff?)
- Falls mehrere Phasen: chronologisch

**Länge:** Max. 2 Sätze

**Bei Vulgärsprache:** Optional (nur wenn historisch relevant)

---

### 2.6 Mechanismus-Analyse (PFLICHT)

```markdown
**Mechanismus-Analyse:**
- ● Inversion (dominant) - Not wird zu Luxus
- ● Kriminalisierung - Recht wird zu Betrug
- ◐ Quantifizierung - teilweise ("Massenmigration")
- ○ Entpolitisierung - nicht vorhanden
```

**Format:**
- `**Mechanismus-Analyse:**` (fett)
- Graduell: `●` (stark), `◐` (teilweise), `○` (nicht vorhanden)
- Mechanismus-Name aus [Werkzeugkasten](WERKZEUGKASTEN.md)
- Kurze Begründung (max. 5 Wörter)

**Hinweis:** Liste nur relevante Mechanismen (3-6). Nicht alle 12 durchgehen.

---

### 2.7 Beispiele / Zitate

**Politische Kampfbegriffe (mit Primärquellen):**

```markdown
**Beispiel:** Hans-Peter Friedrich (CSU, Bundesinnenminister) im Spiegel-Interview März 2013 [@friedrich_2013]: »Wer aber nur kommt, um Sozialleistungen zu kassieren, der missbraucht das Freizügigkeitsrecht. Diesen ==Sozialtourismus== müssen wir unterbinden.« ● Horst Seehofer (CSU) bei der Kreuth-Klausur Januar 2013 [@seehofer_2013]: »Wir werden uns gegen Zuwanderung in die deutschen Sozialsysteme wehren.«
```

**Format:**
- Marker: `●` (Kreis, U+25CF) zwischen Zitaten
- Label: `**Beispiel:**` (fett) **NUR BEIM ERSTEN ZITAT**
- Kontext VOR Zitat: Name (Partei, Funktion) Kontext Datum
- Citekey: `[@nachname_jahr]` (pandoc-citations)
- Zitat: `»...«` (Guillemets)
- Begriff im Zitat: `==Begriff==` (Markdown Highlight)

**Regeln:**
- NUR Original-Zitate von Politikern (keine Kritiker, keine Sekundärquellen!)
- Vollständige Sätze (nicht gekürzt)
- Chronologisch (früheste zuerst)
- Mind. 2-3 Zitate

---

**Vulgärsprache / Umgangssprache (ohne Primärquellen-Pflicht):**

```markdown
**Beispiel:** »Der ist doch nur ein ==Fickfehler==, den wollte keiner.« ● »Hör auf rumzuheulen, du ==Fickfehler==.«
```

**Format:**
- Authentische Verwendungsbeispiele (wie der Begriff wirklich benutzt wird)
- Keine Quellennachweise nötig
- Zeigt Kontext, Wirkung, Verletzungspotential

---

## 3. IPA-PHONETIK (WEB-SAFE)

**Problem:** Kombinierende Diakritika werden auf vielen Plattformen nicht korrekt dargestellt.

### ❌ VERMEIDEN (Standard-IPA, aber problematisch online):

**U+032F (Combining Inverted Breve Below):**
- `i̯`, `u̯` → Zeigt oft "Tofu"-Kästchen

**U+0361 (Combining Double Inverted Breve):**
- `t͡s`, `p͡f`, `d͡ʒ` → Bogen über Buchstaben fehlt oft

---

### ✅ WEB-SAFE (Empfohlen):

**Lösung:** Einfach weglassen. Der Kontext klärt die Aussprache.

| Standard-IPA (problematisch) | Web-Safe (empfohlen) |
|------------------------------|----------------------|
| `[putinˌfɛɐ̯ˈʃteːɐ]` | `[putinˌfɛɐˈʃteːɐ]` |
| `[ʁemiɡʁaˈtsi̯oːn]` | `[ʁemiɡʁaˈtsioːn]` |
| `[zoˈtsi̯aːltuˌʁɪsmʊs]` | `[zoˈtsiaːltuˌʁɪsmʊs]` |
| `[kɔp͡fˌkiːno]` | `[kɔpfˌkiːno]` |

**Merksatz:** Lieber den Bogen weglassen, als ein kaputtes Zeichen riskieren.

---

## 4. CHECKLISTE

**STRUKTUR ✓**
- [ ] Frontmatter (title, language, cssclasses, tags)
- [ ] Headword (H1)
- [ ] Metadaten (H2 mit Middot `·` als Trenner)
- [ ] IPA Web-Safe (keine kombinierenden Diakritika!)
- [ ] Genus ausgeschrieben (DER/DIE/DAS)
- [ ] Zeitangabe + Kategorie
- [ ] HR-Element `---` nach Metadaten
- [ ] Definition (3-4 Sätze: Was? Wirkung? Funktion?)
- [ ] **Mechanismus:** (PFLICHT, max. 2 Sätze)
- [ ] **Mechanismus-Analyse:** (3-6 Mechanismen, graduell)
- [ ] **Beispiel/Zitate:** (mind. 2)

**INHALT ✓**
- [ ] Definition trocken & präzise (keine Moral!)
- [ ] Mechanismus erklärt Wortbestandteile
- [ ] Mechanismus-Analyse: 3-6 relevante (aus [Werkzeugkasten](WERKZEUGKASTEN.md))
- [ ] Graduell: `●` (stark), `◐` (teilweise), `○` (nicht)
- [ ] Zitate/Beispiele authentisch
- [ ] Begriff mit `==Begriff==` hervorgehoben
- [ ] **Politisch:** Primärquellen mit [@citekey]
- [ ] **Vulgär:** Verwendungsbeispiele (keine Quellen nötig)

**STIL ✓**
- [ ] Hauptsätze (keine Nebensatzketten)
- [ ] Verben der Manipulation ("tarnt", "verschleiert")
- [ ] Keine Moral ("zynisch", "perfide" → raus!)
- [ ] Kriegsreporter-Haltung (zeigen, nicht kommentieren)

**TYPOGRAPHIE ✓**
- [ ] Middot `·` als Trenner in H2
- [ ] HR-Element `---` nach Metadaten
- [ ] Guillemets `»«` für Zitate
- [ ] Kreis `●` als Marker
- [ ] Begriff in Zitaten: `==Begriff==` (Markdown Highlight)
- [ ] Fett für **Mechanismus:**, **Geprägt:**, **Beispiel:**

---

## 5. HÄUFIGE FEHLER

### Struktur
❌ Metadaten nicht in H2 (muss H2 sein!)
❌ Genus abgekürzt (DER/DIE/DAS, nicht *m.*)
❌ Fehlendes HR-Element nach Metadaten (`---` ist PFLICHT!)
❌ IPA mit kombinierenden Diakritika (`i̯`, `t͡s` → Web-Safe nutzen!)
❌ Mechanismus fehlt (PFLICHT bei jedem Eintrag!)
❌ Mechanismus-Analyse fehlt (PFLICHT!)

### Inhalt
❌ Zu kurze Definition ("Kampfbegriff für X." - Wirkung fehlt!)
❌ Begriff in Zitaten nicht mit `==Begriff==` markiert
❌ Mechanismus-Analyse ohne Begründung (warum dieser Mechanismus?)
❌ **Politisch:** Sekundärquellen ("Correctiv über X" → nur Original!)
❌ **Politisch:** Kritiker-Zitate (wir suchen Täter, nicht Kritiker!)
❌ **Politisch:** Fehlende [@citekeys] bei Zitaten

### Stil
❌ Moral in Definition ("zynisch", "perfide", "menschenverachtend")
❌ Nebensatzketten (Hauptsätze!)
❌ Superlative ("unglaublich", "extrem")

### Typographie
❌ "Normale Anführungszeichen" statt `»Guillemets«`
❌ Bindestrich `-` statt Middot `·` in H2
❌ **Fett** für Begriff im Zitat statt `==Highlight==`

---

## 6. WORKFLOW

**Schritt 1: Recherche**
- **Politisch:** [RECHERCHE-PROMPT.md](RECHERCHE-PROMPT.md) nutzen → Gemini
- **Vulgär:** Kulturelle Recherche (Etymologie, Verwendung, Kontext)

**Schritt 2: Template kopieren**
- Aus diesem Guide (Abschnitt 1)

**Schritt 3: Schreiben**
- Definition präzise (3-4 Sätze)
- Mechanismus analysieren ([Werkzeugkasten](WERKZEUGKASTEN.md))
- Zitate/Beispiele eintragen
- Begriff mit `==Begriff==` markieren

**Schritt 4: IPA prüfen**
- Web-Safe? Keine `i̯`, `u̯`, `t͡s`, `p͡f`?

**Schritt 5: Checkliste durchgehen**
- Alle Punkte in Abschnitt 4 abhaken

**Schritt 6: Citations verifizieren** (nur politisch)
```bash
python3 wort-fabrik/verify_citations.py
```

---

**Ende der Vorlage.**

*Nach einem Monat wiederkommen: Alles steht hier. Template kopieren, Checkliste abhaken, fertig.*
