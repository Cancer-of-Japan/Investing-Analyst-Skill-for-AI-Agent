#!/usr/bin/env python3
"""Parse TWSE BWIBBU_d JSON (P/E, P/B, dividend yield for all listed stocks).

Usage: parse_bwibbu.py /tmp/bwibbu.json [TICKER,TICKER,...]
"""
import json
import sys

if len(sys.argv) < 2:
    sys.exit("usage: parse_bwibbu.py <json-file> [tickers]")

targets = set(filter(None, sys.argv[2].split(','))) if len(sys.argv) > 2 else None

with open(sys.argv[1]) as f:
    data = json.load(f)

if data.get('stat') != 'OK':
    sys.exit(f"ERROR: BWIBBU_d: {data.get('stat', 'unknown')}")

print('代號|名稱|收盤價|PE|PB|殖利率%|財報年季')
print('-' * 60)
found = set()
for row in data['data']:
    t = row[0].strip()
    if targets and t not in targets:
        continue
    found.add(t)
    print(f'{t}|{row[1]}|Px:{row[2]}|PE:{row[5]}|PB:{row[6]}|DY:{row[3]}|{row[7]}')

if targets:
    missing = targets - found
    if missing:
        print(f'\nNot in TWSE (OTC/invalid): {", ".join(sorted(missing))} -> stockanalysis fallback')
    print(f'Matched: {len(found)}/{len(targets)}')
else:
    print(f'\nTotal: {len(found)} TWSE stocks')
