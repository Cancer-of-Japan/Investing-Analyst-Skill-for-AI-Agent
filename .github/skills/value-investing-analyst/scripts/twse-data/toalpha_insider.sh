#!/bin/bash
# toalpha_insider.sh - Fetch ToAlpha insider trading data
# Usage: ./toalpha_insider.sh [market|<ticker>]
#   market  - market-wide insider summary (top buyers/sellers)
#   <ticker> - per-company insider filings
set -euo pipefail

MODE="${1:-market}"
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'

# ── Market-wide insider summary ──
fetch_market() {
  echo "=== ToAlpha Market-wide Insider Summary ==="
  curl -s 'https://toalpha.tw/insider' -H "User-Agent: $UA" | python3 -c "
import sys, re, html as h

data = sys.stdin.read()
text = re.sub(r'<script[^>]*>.*?</script>', '', data, flags=re.DOTALL)
text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
text = re.sub(r'<[^>]+>', ' ', text)
text = h.unescape(text)
text = re.sub(r'\s+', ' ', text).strip()

# Monthly summary
idx = text.find('全市場買進金額')
if idx >= 0:
    print(text[idx:idx+500])
    print()

# Top 20 net buyers
idx = text.find('淨買超金額前 20')
if idx >= 0:
    print(text[idx:idx+4000])
" 2>/dev/null
}

# ── Per-stock insider filings ──
fetch_stock() {
  local ticker="$1"
  echo "=== ToAlpha insider filings for ${ticker} ==="
  curl -s "https://toalpha.tw/stock/${ticker}/filings" -H "User-Agent: $UA" | python3 -c "
import sys, re, html as h

data = sys.stdin.read()
text = re.sub(r'<script[^>]*>.*?</script>', '', data, flags=re.DOTALL)
text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
text = re.sub(r'<[^>]+>', ' ', text)
text = h.unescape(text)
text = re.sub(r'\s+', ' ', text).strip()

# Extract the main content area
for marker in ['內部人', '買進', '賣出', '申報', '淨買', '淨賣']:
    idx = text.find(marker)
    if idx >= 0:
        start = max(0, idx - 50)
        print(text[start:start + 2000])
        break
else:
    print(f'No insider data found (page length: {len(data)})')
" 2>/dev/null
}

# ── Main ──
case "$MODE" in
  market|--market|-m)
    fetch_market
    ;;
  *)
    fetch_stock "$MODE"
    ;;
esac
