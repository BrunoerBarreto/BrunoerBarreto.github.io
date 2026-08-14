#!/usr/bin/env bash
# Gera os PDFs a partir dos arquivos HTML usando o Chromium em modo headless.
# Uso: ./gerar-pdf.sh
set -euo pipefail

CHROME="${CHROME:-/opt/pw-browsers/chromium-1194/chrome-linux/chrome}"
RAIZ="$(cd "$(dirname "$0")" && pwd)"

render() {
  local html="$1" pdf="$2"
  "$CHROME" --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
    --virtual-time-budget=4000 \
    --print-to-pdf="$pdf" "file://$html" 2>/dev/null
  echo "gerado: $pdf"
}

render "$RAIZ/curriculo/curriculo-brunoer-teles-barreto-filho.html" \
       "$RAIZ/curriculo/curriculo-brunoer-teles-barreto-filho.pdf"

render "$RAIZ/timbrado/papel-timbrado.html" \
       "$RAIZ/timbrado/papel-timbrado.pdf"
