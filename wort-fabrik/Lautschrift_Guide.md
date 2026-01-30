# Best Practices für Lautschrift (IPA) in Markdown-Dateien

Um Darstellungsprobleme (wie "Tofu"-Kästchen oder fehlende Glyphen) auf verschiedenen Plattformen und Browsern zu vermeiden, sollten bei der IPA-Lautschrift folgende Regeln beachtet werden.

## 1. Das Problem: Kombinierende Diakritika
Viele Standard-Webfonts unterstützen komplexe, übereinandergestapelte Zeichen nicht korrekt. Besonders problematisch sind **kombinierende diakritische Zeichen**, die nachträglich an einen Buchstaben "angeklebt" werden.

### Vermeidende Zeichen (Don'ts)
Folgende Unicode-Zeichen verursachen häufig Probleme und sollten **weggelassen** werden:

*   **U+032F (Combining Inverted Breve Below):** Der kleine Bogen *unter* Vokalen für Unsilbigkeit.
    *   *Problem:* `i̯` oder `u̯`
    *   *Lösung:* Einfaches `i` oder `u` verwenden. Der Kontext (Diphthong) klärt meist die Aussprache.
*   **U+0361 (Combining Double Inverted Breve):** Der Bogen *über* zwei Buchstaben (Ligatur-Bogen) für Affrikaten.
    *   *Problem:* `t͡s`, `p͡f`, `d͡ʒ`
    *   *Lösung:* Einfach hintereinander schreiben: `ts`, `pf`, `dʒ`.

## 2. Die Lösung: "Web Safe IPA"
Verwende eine vereinfachte Notation, die nur auf Standard-Zeichen setzt. Die Lesbarkeit bleibt erhalten, die Kompatibilität steigt massiv.

### Beispiele

| Wort | Problematisch (Vermeiden) | Web-Safe (Empfohlen) | Änderung |
| :--- | :--- | :--- | :--- |
| **Putinversteher** | `[...fɛɐ̯...]` | `[...fɛɐ...]` | Bogen unter `ɐ` entfernt |
| **Remigration** | `[...tsi̯oːn]` | `[...tsioːn]` | Bogen unter `i` entfernt |
| **Kopfkino** | `[...kɔp͡f...]` | `[...kɔpf...]` | Bogen über `pf` entfernt |

## 3. Merksatz
> **"Im Zweifel für die Darstellungssicherheit: Lieber den Bogen weglassen, als ein kaputtes Zeichen riskieren."**
