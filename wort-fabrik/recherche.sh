#!/bin/bash

# recherche.sh - Automatisierter Workflow: Recherche → First Draft
# Usage: ./recherche.sh "Begriff"

set -e  # Exit on error

# Check argument
if [ -z "$1" ]; then
  echo "❌ Fehler: Kein Begriff angegeben"
  echo ""
  echo "Usage: ./recherche.sh \"Begriff\""
  echo "Beispiel: ./recherche.sh \"Remigration\""
  exit 1
fi

BEGRIFF="$1"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
RECHERCHE_DIR="$SCRIPT_DIR/Recherche"
DRAFTS_DIR="$SCRIPT_DIR/Drafts"

# Create directories if needed
mkdir -p "$RECHERCHE_DIR" "$DRAFTS_DIR"

# Output files
RECHERCHE_FILE="$RECHERCHE_DIR/Recherche-$BEGRIFF.md"
DRAFT_FILE="$DRAFTS_DIR/Draft-$BEGRIFF.md"

echo ""
echo "🔍 Workflow für: '$BEGRIFF'"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# ============================================
# STEP 1: RECHERCHE
# ============================================
echo "📚 [1/2] Recherchiere Zitate + Mechanismus-Analyse..."
echo ""

# Replace [BEGRIFF HIER EINSETZEN] in RECHERCHE-PROMPT.md and pipe to gemini
sed "s/\[BEGRIFF HIER EINSETZEN\]/$BEGRIFF/g" "$SCRIPT_DIR/RECHERCHE-PROMPT.md" | \
  gemini > "$RECHERCHE_FILE"

if [ ! -s "$RECHERCHE_FILE" ]; then
  echo "❌ Fehler: Recherche-Output ist leer"
  exit 1
fi

echo "   ✓ Recherche gespeichert: $(basename "$RECHERCHE_FILE")"
echo ""

# ============================================
# STEP 2: DRAFT
# ============================================
echo "✍️  [2/2] Schreibe First Draft..."
echo ""

# Read DRAFT-PROMPT.md, insert RECHERCHE_FILE content using sed 'r' command
# This avoids escaping issues with the content itself
sed -e "/\\[RECHERCHE-OUTPUT\\]/r $RECHERCHE_FILE" -e "//d" "$SCRIPT_DIR/DRAFT-PROMPT.md" | \
  gemini > "$DRAFT_FILE"

if [ ! -s "$DRAFT_FILE" ]; then
  echo "❌ Fehler: Draft-Output ist leer"
  exit 1
fi

echo "   ✓ Draft gespeichert: $(basename "$DRAFT_FILE")"
echo ""

# ============================================
# STEP 3: EXTRACT BIBTEX
# ============================================
echo "📚 [3/3] Extrahiere BibTeX-Einträge für Zotero..."
echo ""

IMPORTS_DIR="$SCRIPT_DIR/imports"
TO_ZOTERO_FILE="$IMPORTS_DIR/to_zotero.bib"

# Create imports dir if needed
mkdir -p "$IMPORTS_DIR"

# Extract BibTeX blocks from Recherche output and APPEND to to_zotero.bib
# Format: ```bibtex ... ```
if grep -q '```bibtex' "$RECHERCHE_FILE"; then
  # Add separator and comment
  echo "" >> "$TO_ZOTERO_FILE"
  echo "% ========================================" >> "$TO_ZOTERO_FILE"
  echo "% From: Recherche-$BEGRIFF.md ($(date '+%Y-%m-%d %H:%M'))" >> "$TO_ZOTERO_FILE"
  echo "% ========================================" >> "$TO_ZOTERO_FILE"
  echo "" >> "$TO_ZOTERO_FILE"

  # Extract BibTeX content (between ```bibtex and ```)
  sed -n '/```bibtex/,/```/p' "$RECHERCHE_FILE" | sed '1d;$d' >> "$TO_ZOTERO_FILE"

  echo "   ✓ BibTeX extrahiert: $(basename "$TO_ZOTERO_FILE")"
else
  echo "   ⚠ Keine BibTeX-Einträge gefunden"
fi
echo ""

# ============================================
# DONE
# ============================================
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ Workflow abgeschlossen!"
echo ""
echo "📄 Outputs:"
echo "   Recherche: $RECHERCHE_FILE"
echo "   Draft:     $DRAFT_FILE"
echo "   BibTeX:    $TO_ZOTERO_FILE"
echo ""
echo "🔄 Nächste Schritte:"
echo "   1. Draft öffnen: open \"$DRAFT_FILE\""
echo "   2. Mit Claude überarbeiten"
echo "   3. Triple-Verification (Zitate prüfen!)"
echo "   4. Zotero: Import $TO_ZOTERO_FILE → bibliography.bib"
echo "   5. verify_citations.py laufen lassen"
echo ""
