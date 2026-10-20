#!/usr/bin/env python3
"""Parse MoatMap best-stocks/taiwan page (reads HTML from stdin).

Extracts the StockRank top-25 table: rank, ticker, name, sector, mcap,
yield, P/E, StockRank score + Quality/Value/Momentum sub-scores, style.

Usage: curl -s <url> -H 'User-Agent: ...' | parse_moatmap.py
"""
import html as h
import re
import sys

data = sys.stdin.read()

if len(data) < 50000:
    print(f'  (page too short: {len(data)} bytes - likely blocked/redirect)')
    sys.exit(0)

# Table begins at the Yield header
hdr = data.find('>Yield<')
if hdr < 0:
    print('  (ranking table not found - page structure changed)')
    sys.exit(0)

rows = []
for m in re.finditer(r'<tr[\s>]', data[hdr:]):
    start = hdr + m.start()
    end = data.find('</tr>', start)
    if end < 0:
        continue
    block = data[start:end]
    rows.append(block)

print('排名|代號|名稱|產業|市值|殖利率|PE|Score|Q|V|M|風格')
print('-' * 90)
count = 0
for block in rows:
    tkr = re.search(r'href="/stock/(\d{4}\.TWO?)"', block)
    if not tkr:
        continue  # header or malformed row
    rank_m = re.search(r'<td[^>]*tabular-nums[^>]*>(\d+)</td>', block)
    name_m = re.search(r'title="([^"]+)"[^>]*class="[^"]*text-muted-strong|group-hover:text-accent-hover" title="([^"]+)"', block)
    name = (name_m.group(1) or name_m.group(2)) if name_m else '?'
    sec_m = re.search(r'>(TW|TWO) · ([^·<]+) · (\$[\d.]+[BM])<', block)
    yield_m = re.search(r'Yield </span>([\d.%]+)', block)
    pe_m = re.search(r'P/E </span>([\d.%]+)', block)
    # Score circles: font-bold">N</span> then label Score/Q/V/M
    scores = re.findall(
        r'font-bold">(\d+)</span></div><span[^>]*>(Score|Q|V|M)</span>',
        block,
    )
    sdict = {label: val for val, label in scores}
    style_m = re.search(r'data-stock-style="\w+"[^>]*><span translate="no">([^<]+)</span>', block)

    print('|'.join([
        rank_m.group(1) if rank_m else '?',
        tkr.group(1),
        h.unescape(name),
        sec_m.group(2).strip() if sec_m else '?',
        sec_m.group(3) if sec_m else '?',
        yield_m.group(1) if yield_m else 'N/A',
        pe_m.group(1) if pe_m else 'N/A',
        sdict.get('Score', '?'),
        sdict.get('Q', '?'),
        sdict.get('V', '?'),
        sdict.get('M', '?'),
        style_m.group(1) if style_m else '',
    ]))
    count += 1

print(f'\nTotal: {count} stocks (source: moatmap.ai/best-stocks/taiwan, edition 2026-10-01)')
