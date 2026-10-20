#!/bin/bash
# insider_lookup.sh - Look up insider buy/sell for TWSE stocks
# Usage: ./insider_lookup.sh <ticker>
# Source: ToAlpha (reliable, no JS rendering needed)
# Data lag: ~1.5 months (MOPS monthly filing due by 15th)
set -euo pipefail

TICKER="${1:?Usage: $0 <ticker>}"
UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'

fetch_toalpha() {
  local ticker="$1"
  curl -s "https://toalpha.tw/stock/${ticker}/filings" \
    -H "User-Agent: $UA" \
    | python3 -c "
import sys, re, html as h

data = sys.stdin.read()
text = re.sub(r'<script[^>]*>.*?</script>', '', data, flags=re.DOTALL)
text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL)
text = re.sub(r'<[^>]+>', ' ', text)
text = h.unescape(text)
text = re.sub(r'\s+', ' ', text).strip()

# Extract company name
name_m = re.search(r'(\S+\(\d+\))\s*申報資料', text)
name = name_m.group(1) if name_m else '${ticker}'

# Extract key metrics
results = {}

# 董監持股比
m = re.search(r'董監持股比.*?(\d+\.?\d*)%.*?一年來\s*([+\-]\d+\.?\d*)', text)
if m: results['董監持股比'] = f'{m.group(1)}% (YoY {m.group(2)}pp)'

# 質押比
m = re.search(r'質押比.*?(\d+\.?\d*)%', text)
if m: results['質押比'] = f'{m.group(1)}%'

# 近 6 個月淨買賣
m = re.search(r'近 6 個月淨買賣.*?集中市場\s*([+\-][\d,]+)\s*萬\s*([+\-]\d+)\s*張', text)
if m: results['近6月淨買賣'] = f'{m.group(1)}萬 ({m.group(2)}張)'

# 近 12 個月淨買賣
m = re.search(r'近 12 個月淨買賣.*?集中市場\s*([+\-][\d,]+)\s*萬\s*([+\-]\d+)\s*張', text)
if m: results['近12月淨買賣'] = f'{m.group(1)}萬 ({m.group(2)}張)'

# 買進/賣出 breakdown
m = re.search(r'買進\s*(\d+)\s*張\s*\(\s*([\d,]+)\s*萬\s*\).*?賣出\s*(\d+)\s*張\s*\(\s*([\d,]+)\s*萬', text)
if m: results['12月買/賣'] = f'買{m.group(1)}張({m.group(2)}萬) / 賣{m.group(3)}張({m.group(4)}萬)'

print(f'=== {name} — 內部人買賣摘要 ===')
for k, v in results.items():
    print(f'  {k}: {v}')
if not results:
    print('  (no data parsed)')
print(f'  Source: toalpha.tw/stock/{\"${ticker}\"}/filings (資料至 2026/09)')
" 2>/dev/null || echo "Fetch failed for ${ticker}"
}

fetch_toalpha "$TICKER"
