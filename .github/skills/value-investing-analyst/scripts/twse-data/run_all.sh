#!/bin/bash
# run_all.sh - Run all TWSE data collectors in sequence
# Usage: ./run_all.sh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
OUTPUT_DIR="${SCRIPT_DIR}/output"
mkdir -p "$OUTPUT_DIR"

echo "============================================"
echo " TWSE Data Collection - $(date '+%Y-%m-%d %H:%M:%S')"
echo "============================================"

# 1. TWSE openapi - P/E, P/B, yield for all stocks
echo ""
echo "[1/5] TWSE BWIBBU (P/E, P/B, yield)..."
bash "$SCRIPT_DIR/fetch_stock_data.sh" > "$OUTPUT_DIR/bwibbu_all.txt" 2>&1
echo "  -> output/bwibbu_all.txt ($(wc -l < "$OUTPUT_DIR/bwibbu_all.txt") lines)"

# 2. MoatMap StockRank
echo ""
echo "[2/5] MoatMap StockRank..."
bash "$SCRIPT_DIR/moatmap_scrape.sh" > "$OUTPUT_DIR/moatmap_top25.txt" 2>&1
echo "  -> output/moatmap_top25.txt"

# 3. FairValue Calculator undervalued list
echo ""
echo "[3/5] FairValue undervalued stocks..."
bash "$SCRIPT_DIR/fairvalue_scrape.sh" > "$OUTPUT_DIR/fairvalue_undervalued.txt" 2>&1
echo "  -> output/fairvalue_undervalued.txt"

# 4. ToAlpha market-wide insider
echo ""
echo "[4/5] ToAlpha market insider summary..."
bash "$SCRIPT_DIR/toalpha_insider.sh" market > "$OUTPUT_DIR/toalpha_market_insider.txt" 2>&1
echo "  -> output/toalpha_market_insider.txt"

# 5. Per-stock insider lookups for target tickers
TICKERS="${1:-1476,6206,8016,2006,5609,2546,5515,3005,2474,5871}"
echo ""
echo "[5/5] Per-stock insider filings for: $TICKERS"
INSIDER_DIR="$OUTPUT_DIR/insider"
mkdir -p "$INSIDER_DIR"
for t in $(echo "$TICKERS" | tr ',' ' '); do
  bash "$SCRIPT_DIR/insider_lookup.sh" "$t" > "$INSIDER_DIR/${t}.txt" 2>&1
  echo "  -> insider/${t}.txt"
done

echo ""
echo "============================================"
echo " Done! Output in: $OUTPUT_DIR/"
echo "============================================"
echo ""
echo "Summary of outputs:"
ls -lh "$OUTPUT_DIR"/ "$INSIDER_DIR"/ 2>/dev/null | grep -v '^total'
