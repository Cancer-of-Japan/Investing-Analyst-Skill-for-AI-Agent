# TWSE Data Collection Scripts

Scripts and commands used to collect Taiwan Stock Exchange data for stock analysis
(value-investing-analyst skill sessions, Oct 2026).

## Quick start

```bash
./run_all.sh                              # full pipeline -> ./output/
./fetch_stock_data.sh 1476,5609           # P/E, P/B, yield + deep stats (per ticker)
./insider_lookup.sh 5515                  # insider buy/sell summary (per ticker)
./moatmap_scrape.sh                       # StockRank top-25 table
./toalpha_insider.sh market               # market-wide insider top-20 buyers/sellers
./fairvalue_scrape.sh                     # undervalued list (Cloudflare: see note)
```

## Files

| File | Purpose | Status |
|------|---------|--------|
| `run_all.sh` | Run all collectors -> `output/` | works |
| `fetch_stock_data.sh` | P/E, P/B, yield (all TWSE) + deep stats per ticker | works |
| `parse_bwibbu.py` | Parse TWSE BWIBBU_d JSON | works |
| `parse_stockanalysis.py` | Parse stockanalysis.com statistics (stdin) | works |
| `insider_lookup.sh` | Per-stock insider buy/sell summary | works |
| `toalpha_insider.sh` | Market-wide + per-stock insider (ToAlpha) | works |
| `moatmap_scrape.sh` | MoatMap StockRank top-25 table | works |
| `parse_moatmap.py` | Parse MoatMap ranking table (stdin) | works |
| `fairvalue_scrape.sh` | FairValue undervalued list | Cloudflare-blocked; detects and prints alternatives |
| `search_queries.md` | Web search queries used for stock discovery | reference |

## Data sources (endpoints that actually work)

| Source | Endpoint | Data |
|--------|----------|------|
| TWSE openapi | `https://www.twse.com.tw/exchangeReport/BWIBBU_d?response=json&selectDate=20261016` | All TWSE: close price, yield, P/E, P/B, fiscal period (TTM, 4Q) |
| stockanalysis.com | `https://stockanalysis.com/quote/tpe/{TICKER}/statistics/` (TWSE) or `/quote/tpex/{TICKER}/` (OTC) | ROE/ROA/ROIC, margins, current ratio, payout, EV. Note: table rows use `<span><!---->Label<!----></span>` + `title="value"` markup; Cloudflare occasionally challenges — retry with full browser UA |
| MoatMap | `https://moatmap.ai/best-stocks/taiwan` | Monthly StockRank top-25: yield, P/E, Score/Q/V/M, style tag (data in HTML table, not JSON) |
| ToAlpha | `https://toalpha.tw/stock/{TICKER}/filings` | Per-stock insider: 董監持股比, 質押比, 6/12-month net buy/sell (張/萬) |
| ToAlpha | `https://toalpha.tw/insider` | Market-wide monthly insider totals, top-20 net buyers/sellers, streaks |
| FairValue Calc | `https://www.fairvalue-calculator.com/undervalued-stocks/taiwan` | Fair-value upside, quality score — **Cloudflare JS challenge; use opencode WebFetch tool or browser** |

## Dead / unusable endpoints (learned the hard way)

- `https://www.twse.com.tw/openapi/v1/exchange/bwibbu_all` → 307 redirect / gone (use `BWIBBU_d`)
- `https://www.twse.com.tw/exchangeReport/BWIBBU?...` → "沒有符合條件的資料" (use `BWIBBU_d`)
- MOPS (`mopsov.twse.com.tw`, `mops.twse.com.tw/mops`) → JS SPA, curl gets empty form; old CGI `server-java/t56sb01` → 404
- TPEX openapi / `tpex.org.tw/web/stock/...` → SPA shell or 404
- FairValue `/undervalued-stocks.csv` and `.json` → also Cloudflare-protected

## Notes

- TWSE dates: `selectDate=20261016` (YYYYMMDD) works on BWIBBU_d; ROC dates also accepted.
- OTC stocks (e.g. 5609 中菲行 = TPEX) are NOT in BWIBBU_d — `fetch_stock_data.sh`
  falls back to stockanalysis `/quote/tpex/` automatically (detects 404).
- Insider data lag: MOPS monthly filings due by the 15th of the following month
  (ToAlpha shows "資料至 2026/09" as of 2026-10-19).
- Dividend yield / P/E are trailing (TTM), financial period shown as `ROC年/季` (e.g. `115/2` = 2026 Q2).
