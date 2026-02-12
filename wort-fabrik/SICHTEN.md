# SICHTEN: DIP-Recherche → KONTEXT-Material

**Aufgabe:** Wähle aus `DIP-[Begriff].md` die besten 12–15 Zitate und schreibe sie als
`Recherche/[Begriff]/KONTEXT-[Begriff].md` — direkt nutzbar für DRAFT.md und Zotero-Import.

**Input:** [DIP-[Begriff].md einfügen]

---

## ⚠️ ABSOLUTES VERBOT

**Zitate NIEMALS verändern.** Kein Kürzen, kein Paraphrasieren, kein Zusammenfassen.
Jedes Zitat muss wortidentisch aus der DIP-Datei übernommen werden — inklusive `[…]`-Markierungen.

---

## DIE 11 AUSWAHLKRITERIEN

**Grundsatz: Zitat-Qualität > Prominenz**

### 1. Zeigt das Zitat die innere Kausalität des Sprechers? (Gewicht: Sehr hoch)

Das wichtigste Kriterium. Ein gutes Zitat zeigt nicht nur *dass* der Begriff verwendet wird,
sondern *warum* der Sprecher ihn für berechtigt hält — die Logik dahinter.

❌ Wertlos: »Das ist Gutmenschentum.«
✅ Wertvoll: »Das ist Gutmenschentum — wer solche Forderungen stellt, kennt die Folgen nicht.«

### 2. Qualität / Aussagekraft (Gewicht: Sehr hoch)

**Gut:** argumentativ, konkret, klare Positionierung, bringt neue Perspektive
**Schlecht:** banal ("Wir sollten darüber reden"), leer (keine Argumentation), reine Wiederholung

### 3. Art der Verwendung — PFLICHT: Balance (Gewicht: Sehr hoch)

- `[A]` **Affirmativ:** Sprecher verwendet Begriff selbst als eigenes Wort
- `[K]` **Kritisch/Metasprachlich:** Sprecher lehnt Begriff ab, analysiert ihn, zitiert ihn distanziert

**Pflicht:** Mindestens 4–5 affirmative Zitate. Ohne sie fehlt die Etablierungsgeschichte.

### 4. Zeitliche Spreizung (Gewicht: Hoch)

Zeige die Entwicklung des Begriffs. Angestrebte Verteilung:
- Frühe Phase (Erstverwendung / Etablierung)
- Hochphase / Kontroverse
- Aktuelle Verwendung

Nicht mehr als 3 Zitate aus demselben Jahr.

### 5. Primärzitat bevorzugen (Gewicht: Hoch)

Sprecher verwendet Begriff **selbst** > Sprecher zitiert jemand anderen (Sekundärzitat).
Sekundärzitate (`"X sagte..."`) nur wenn inhaltlich unverzichtbar.

### 6. Prominenz des Sprechers (Gewicht: Mittel — nachrangig zu Qualität)

Rangfolge bei gleicher Zitat-Qualität:
1. Bundeskanzler / Bundespräsident
2. Minister (Bundesregierung)
3. Staatssekretäre / Fraktionsvorsitzende
4. Bekannte Abgeordnete (langjährig, Ex-Minister)
5. Reguläre Abgeordnete

Ein gutes Zitat eines Hinterbänklers schlägt ein banales Ministeriums-Zitat.

### 7. Zentralität im Absatz (Gewicht: Mittel)

Ist der Begriff Kern der Aussage — oder fällt er beiläufig am Rand?
Randerwähnungen deprioritisieren.

### 8. Fragment-Malus (Gewicht: Mittel)

`[…]`-Zitate zeigen: Rede beginnt mid-sentence, Kontext unvollständig.
Nur wählen wenn inhaltlich unverzichtbar und kein vollständiges Zitat für dieselbe Position existiert.

### 9. Zitat-Länge: Kontext bevorzugen (Gewicht: Mittel)

2–4 Sätze mit Kontext > 1 Satz isoliert. Beim Schreiben kürzen wir — beim Sichten nicht.
Zu lange Zitate (5+ verschachtelte Sätze) ebenfalls deprioritisieren.

### 10. Kontext-Integrität (Gewicht: Sehr hoch)

Zitat darf den Sprecher nicht entstellen.
❌ Sprecher sagt: "Das ist KEIN Gutmenschentum!" → Zitat zeigt: "[…] Gutmenschentum!"

### 11. Partei-Diversität (Gewicht: Niedrig)

Nicht alles von derselben Partei, wenn Alternativen gleicher Qualität vorhanden.

---

## AUSWAHLPROZESS

1. **Lies alle Zitate** aus der DIP-Datei — alle, nicht nur die ersten.
2. **Kategorisiere grob:** A (affirmativ) oder K (kritisch/metasprachlich)
3. **Prüfe Kriterien 1–3** (die drei gewichtigsten) für jeden Kandidaten
4. **Prüfe zeitliche Spreizung:** Welche Jahre sind vertreten? Lücken?
5. **Finale Auswahl:** 12–15 Zitate, chronologisch geordnet

---

## OUTPUT-FORMAT (exakt einhalten)

```markdown
# KONTEXT-MATERIAL: [Begriff]

*[X] Zitate · [X] affirmativ [A] · [X] kritisch/metasprachlich [K] · [Jahr]–[Jahr]*

---

**1.** `[A]` **[Vorname Nachname]** ([Partei/Funktion], [JJJJ-MM-TT]) · BT [WP]/[Nr]
»[Zitat exakt aus DIP-Datei]«
`[citekey]`

**2.** `[K]` **[Vorname Nachname]** ([Partei/Funktion], [JJJJ-MM-TT]) · BT [WP]/[Nr]
»[Zitat exakt aus DIP-Datei]«
`[citekey]`

[... bis 12–15]

---

## Citekeys (→ to_zotero.bib)

`citekey_1` `citekey_2` `citekey_3` [alle auf einer Zeile]

---

## BibTeX (→ to_zotero.bib)

```bibtex
[Vollständige v5.2-BibTeX-Einträge aller ausgewählten Zitate — exakt aus DIP-Datei kopieren]
```
```

---

## REGELN

- **Chronologische Reihenfolge:** Ältestes Zitat zuerst, jüngstes zuletzt
- **Globale Nummerierung:** 1–15 (nicht neu beginnend pro Kategorie)
- **Kategorie-Label** `[A]` oder `[K]` steht direkt hinter der Nummer
- **Zitate exakt** aus DIP-Datei — kein Wort verändern
- **Citekeys** exakt aus DIP-Datei — Format `nachname_jjjj_mm_tt`
- **BibTeX exakt** aus DIP-Datei — vollständige v5.2-Einträge (title, shorttitle, langid, etc.)
- **Keine Begründungen** im Output — nur die Zitate, keine Meta-Kommentare

---

## STARTE HIER

**Begriff:** [EINSETZEN]

**Schreibe den Output in die Datei:**
`Recherche/[Begriff]/KONTEXT-[Begriff].md`

**Ausgabe im Chat:**
`✓ SICHTEN abgeschlossen: [X] Zitate ([X] affirmativ, [X] kritisch) · [Jahr]–[Jahr]`
