#!/usr/bin/env python3
"""Parse stockanalysis.com statistics page (reads HTML from stdin).

Gives ROE/margins/growth/FCF for deep stats, and valuation fallback
for OTC stocks not covered by TWSE BWIBBU_d.

Usage: curl -s <url> -H 'User-Agent: ...' | parse_stockanalysis.py
"""
import html as h
import re
import sys

data = sys.stdin.read()

if 'Just a moment' in data[:3000]:
    print('  BLOCKED by Cloudflare - retry later or use browser')
    sys.exit(0)

# Table rows: <span><!---->Label<!----></span> ... <td title="value">
results = {}
for m in re.finditer(r'<span><!---->([^<]+)<!----></span>', data):
    label = h.unescape(m.group(1)).strip()
    v = re.search(r'title="([^"]+)"', data[m.end():m.end() + 600])
    if v:
        results[label] = v.group(1)

want = [
    'PE Ratio', 'Forward PE', 'P/B Ratio', 'Price to Free Cash Flow',
    'Return on Equity (ROE)', 'Return on Assets (ROA)', 'Return on Invested Capital (ROIC)',
    'Debt / Equity Ratio', 'Current Ratio', 'Quick Ratio',
    'Market Cap', 'Enterprise Value',
    'Dividend Yield', 'Payout Ratio',
    'Operating Margin', 'Net Profit Margin', 'Gross Margin',
    'Revenue Growth', 'EPS Growth', 'Free Cash Flow Yield',
]
printed = 0
for w in want:
    if w in results:
        print(f'  {w}: {results[w]}')
        printed += 1

m = re.search(r'<title>([^<]+)</title>', data)
if m:
    print(f'  Name: {h.unescape(m.group(1)).split("-")[0].strip()}')
if printed == 0:
    print(f'  (no rows parsed, page length {len(data)})')
