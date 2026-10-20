#!/bin/bash
# moatmap_scrape.sh - Fetch MoatMap StockRank top-25 Taiwan stocks
# Usage: ./moatmap_scrape.sh
# Data: rank, ticker, yield, P/E, StockRank (Quality/Value/Momentum), style
# Edition: monthly (current: 2026-10-01)
set -euo pipefail

DIR="$(cd "$(dirname "$0")" && pwd)"

echo "Fetching MoatMap best Taiwan stocks..."
curl -s 'https://moatmap.ai/best-stocks/taiwan' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36' \
  | python3 "$DIR/parse_moatmap.py"
