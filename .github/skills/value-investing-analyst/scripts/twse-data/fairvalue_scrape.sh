#!/bin/bash
# fairvalue_scrape.sh - Fetch FairValue Calculator undervalued Taiwan stocks
# Usage: ./fairvalue_scrape.sh
# Data: fair-value upside, quality score for undervalued TWSE/TPEx stocks
#
# NOTE: fairvalue-calculator.com is behind Cloudflare JS challenge;
#       plain curl gets "Just a moment..." (no body). Options:
#       1. Use the opencode WebFetch tool (works)
#       2. Open in a browser
set -euo pipefail

UA='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'

echo "Fetching FairValue Calculator undervalued Taiwan stocks..."
BODY="$(curl -s 'https://www.fairvalue-calculator.com/undervalued-stocks/taiwan' \
  -H "User-Agent: $UA" -H 'Accept: text/html,application/xhtml+xml')"

if grep -q 'Just a moment' <<<"$BODY"; then
  echo "BLOCKED: Cloudflare JS challenge (plain curl cannot solve it)."
  echo "Alternatives:"
  echo "  - opencode WebFetch tool on: https://www.fairvalue-calculator.com/undervalued-stocks/taiwan"
  echo "  - Browser: same URL"
  echo "  - CSV/JSON exports (also Cloudflare-protected):"
  echo "      https://www.fairvalue-calculator.com/undervalued-stocks.csv"
  echo "      https://www.fairvalue-calculator.com/undervalued-stocks.json"
  exit 0
fi

printf '%s' "$BODY" | python3 -c "
import sys, re, html as h
data = sys.stdin.read()
pairs = re.findall(
    r'href=\"/\?q=(\d+)\.(?:TWO?|TW)\"[^>]*>([^<]+)</a>.*?'
    r'Quality\s*(\d+).*?Upside\s*\+?([\d.]+%)',
    data, re.DOTALL)
if not pairs:
    print(f'Could not parse (page length {len(data)}) - structure may have changed')
else:
    print('代號|名稱|Quality|Upside')
    for t, name, q, up in pairs[:30]:
        print(f'{t}|{h.unescape(name).strip()}|{q}|{up}')
"
