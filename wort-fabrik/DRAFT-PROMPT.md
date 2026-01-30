# DRAFT-PROMPT: Wörterbuch-Eintrag schreiben

**An:** Gemini (oder andere AI)
**Aufgabe:** Vollständigen Wörterbuch-Eintrag schreiben basierend auf Recherche-Output

---

## INPUT: RECHERCHE-ERGEBNIS

Du hast gerade eine Recherche zu einem politischen Kampfbegriff durchgeführt. Hier ist das vollständige Ergebnis:

---

[RECHERCHE-OUTPUT]

---

## AUFGABE

Schreibe einen **vollständigen Wörterbuch-Eintrag** im Markdown-Format basierend auf dieser Recherche.

---

## FORMAT-VORLAGE

```markdown
---
title: [Begriff]
language: de
cssclasses: dictionary-entry
tags:
  - Kampfbegriff
  - [Mechanismus 1]
  - [Mechanismus 2]
---

# [Begriff]

## [IPA] · GENUS · Zeitangabe · Kategorie

---

[Definition: 3-4 Sätze. Was ist es? Wirkung? Funktion?]

**Mechanismus:** "[Teil 1]" (Bedeutung) + "[Teil 2]" (Bedeutung) = Wirkung.

**Geprägt:** [Name/Partei (Jahr), Kontext]

**Mechanismus-Analyse:**
- ● [Mechanismus 1] (dominant) - [Begründung]
- ● [Mechanismus 2] - [Begründung]
- ◐ [Mechanismus 3] (teilweise) - [Begründung]

**Beispiel:** [Name (Partei, Funktion) Kontext Datum [@citekey]: »Zitat mit ==Begriff==.« ● [Weiteres Zitat] [@citekey2]: »...«
```

---

## REGELN

### 1. Frontmatter
- **title:** Genau wie Begriff (z.B. "Sozialtourismus")
- **tags:** "Kampfbegriff" + 1-2 dominante Mechanismen

### 2. IPA-Phonetik (Web-Safe!)
- **WICHTIG:** Keine kombinierenden Diakritika!
- ❌ VERMEIDEN: `i̯`, `u̯`, `t͡s`, `p͡f`
- ✅ WEB-SAFE: `i`, `u`, `ts`, `pf`
- Betonung: `ˈ` vor betonter Silbe
- Lange Vokale: `ː`

**Beispiele:**
- "Sozialtourismus" → `[zoˈtsiaːltuˌʁɪsmʊs]` (NICHT `[zoˈtsi̯aːl...]`)
- "Remigration" → `[ʁemiɡʁaˈtsioːn]` (NICHT `[...tsi̯oːn]`)

### 3. Metadaten-Zeile
- Format: `## [IPA] · GENUS · Zeitangabe · Kategorie`
- Middot `·` als Trenner (Option+Shift+9 auf Mac)
- Genus ausgeschrieben: DER/DIE/DAS
- Zeitangabe: `politisch, ab JAHR`
- Kategorie: Dysphemismus/Euphemismus/Kampfbegriff

### 4. Definition (3-4 Sätze)
- Hauptsätze (kurz, prägnant)
- Verben der Manipulation: "tarnt", "verschleiert", "kriminalisiert", "entmenschlicht"
- **KEINE Moral:** "zynisch", "perfide" → raus!
- **Kriegsreporter-Haltung:** Zeigen, nicht kommentieren

### 5. Mechanismus
- Format: `**Mechanismus:** "Teil1" (Bedeutung) + "Teil2" (Bedeutung) = Wirkung.`
- Erklärt Wortbestandteile
- Max. 2 Sätze

### 6. Geprägt
- Format: `**Geprägt:** Name/Partei (Jahr), Kontext`
- Max. 2 Sätze
- Chronologisch bei mehreren Phasen

### 7. Mechanismus-Analyse
- Graduell: `●` (stark), `◐` (teilweise), `○` (nicht vorhanden)
- 3-6 relevante Mechanismen (nicht alle 12!)
- Kurze Begründung (max. 5 Wörter)
- Dominanter Mechanismus zuerst

### 8. Zitate
- Format: `**Beispiel:** Name (Partei, Funktion) Kontext Datum [@citekey]: »Zitat.«`
- Marker zwischen Zitaten: `●` (Kreis, U+25CF)
- Label `**Beispiel:**` nur beim ersten Zitat
- Citekeys: `[@nachname_jahr]` (pandoc-citations)
- Begriff im Zitat: `==Begriff==` (Markdown Highlight)
- Guillemets: `»«` (nicht "normale Anführungszeichen")

---

## STIL-VORGABEN

### ✅ DO:
- Hauptsätze (ein Gedanke pro Satz)
- Kurz & präzise (lieber 2 Sätze klar als 10 schwafeln)
- Verben vor Nomen ("verschleiert" statt "Verschleierung")
- Aktiv statt Passiv ("kriminalisiert" statt "wird kriminalisiert")
- Spezifisch ("CSU 2013" statt "Konservative")

### ❌ DON'T:
- Nebensatzketten
- Nominalisierungen ("Die Verwendung erfolgt" → "Menschen nutzen")
- Superlative ("fantastisch", "extrem", "unglaublich")
- Moral ("zynisch", "perfide", "menschenverachtend")
- Enthusiasmus ("wichtig!", "beachtenswert")

---

## QUALITÄTSKRITERIEN

**Dein Eintrag muss erfüllen:**

✅ Alle Zitate aus der Recherche übernommen (mit [@citekeys])
✅ Mechanismus-Analyse graduell (●◐○)
✅ IPA Web-Safe (keine `i̯`, `u̯`, `t͡s`)
✅ Kriegsreporter-Stil (trocken, keine Moral)
✅ Struktur exakt wie Vorlage
✅ Begriff in Zitaten mit `==Begriff==` markiert
✅ HR-Element `---` nach Metadaten

---

## BEISPIEL-OUTPUT (Referenz)

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
- ● Inversion (dominant) - Not → Luxus
- ● Kriminalisierung - Recht → Betrug
- ● Ethnisierung - Ziel: Osteuropäer/Roma
- ● Euphemismus - "Tourismus" harmlos
- ◐ Quantifizierung - teilweise ("Massenmigration")

**Beispiel:** Hans-Peter Friedrich (CSU, Bundesinnenminister) im Spiegel-Interview März 2013 [@friedrich_2013]: »Wer aber nur kommt, um Sozialleistungen zu kassieren, der missbraucht das Freizügigkeitsrecht. Diesen ==Sozialtourismus== müssen wir unterbinden.« ● Horst Seehofer (CSU) bei der Kreuth-Klausur Januar 2013 [@seehofer_2013]: »Wir werden uns gegen Zuwanderung in die deutschen Sozialsysteme wehren – bis zur letzten Patrone.«
```

---

## STARTBEFEHL

**Schreibe jetzt den vollständigen Wörterbuch-Eintrag basierend auf der Recherche oben.**

**Wichtig:**
- Nutze ALLE Zitate aus der Recherche
- IPA Web-Safe (keine `i̯`, `u̯`)
- Kriegsreporter-Stil (trocken, keine Moral)
- Exakte Struktur wie Vorlage
