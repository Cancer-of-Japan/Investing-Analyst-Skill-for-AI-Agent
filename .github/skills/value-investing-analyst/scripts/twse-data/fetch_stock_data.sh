#!/bin/bash
# fetch_stock_data.sh - Fetch TWSE stock valuation data
# Usage:
#   ./fetch_stock_data.sh              # All TWSE stocks (P/E, P/B, yield)
#   ./fetch_stock_data.sh 2451,1476    # Specific tickers (+ deep stats each)
# Data:
#   - TWSE BWIBBU_d openapi: P/E, P/B, dividend yield (TTM, 4-quarter)
#   - stockanalysis.com: ROE, margins, growth, FCF, OTC fallback
# Note: OTC (TPEX) stocks are NOT in BWIBBU_d; they use stockanalysis only.
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"
TICKERS="${1:-}"
UA_STOCKANALYSIS='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

# ── TWSE BWIBBU_d: P/E, P/B, yield for all listed stocks ──
fetch_bwibbu() {
  curl -s 'https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=json&selectDate=20261016&sort=0&order=desc' \
    -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)' > /tmp/bwibbu.json
  python3 "$DIR/parse_bwibbu.py" /tmp/bwibbu.json "$TICKERS"
}

# ── stockanalysis.com statistics (deep stats / OTC fallback) ──
# URL scheme: /quote/tpe/ = TWSE, /quote/tpex/ = OTC (TPEX)
fetch_stockanalysis() {
  local ticker="$1"
  echo ""
  echo "=== ${ticker} (stockanalysis.com) ==="
  local html
  html="$(curl -s "https://stockanalysis.com/quote/tpe/${ticker}/statistics/" \
    -H "User-Agent: $UA_STOCKANALYSIS")"
  if grep -q '<title>404' <<<"$html"; then
    html="$(curl -s "https://stockanalysis.com/quote/tpex/${ticker}/statistics/" \
      -H "User-Agent: $UA_STOCKANALYSIS")"
  fi
  printf '%s' "$html" | python3 "$DIR/parse_stockanalysis.py"
}

# ── Main ──
fetch_bwibbu
for t in $(echo "$TICKERS" | tr ',' ' '); do
  [ -n "$t" ] && fetch_stockanalysis "$t"
done
