---
name: value-investing-analyst
description: 'Analyze stocks, funds, and portfolios using the frameworks of Graham, Lynch, Buffett, Munger, Icahn, Bogle, Dalio, Simons, and Soros. Use when the user asks things like: "is this stock a buy", "should I buy/sell/hold X", "is X undervalued or overvalued", "what is the intrinsic value / fair value of X", "Graham number", "PEG ratio", "owner earnings", "margin of safety", "what category is this stock" (Lynch slow grower/stalwart/fast grower/cyclical/turnaround/asset play), "does X have a moat", "review my portfolio", "asset allocation", "diversification", "rebalance my portfolio", "index fund vs active fund vs ETF", "fund costs/expense ratio", "is this a bubble", "quant/backtested strategy evaluation", "activist/asset-value situation", "accounting red flags", "cognitive biases in my thesis", or "pick stocks from this list / screen / CSV".'
---

# Value Investing Analyst (Graham + Lynch + Buffett + Munger + Icahn + Bogle + Dalio + Simons + Soros)

Evaluate investments the way these masters would, then reconcile their views into one verdict. Graham, Lynch, Buffett, and Munger are the **core lenses** for any single-stock analysis. Icahn, Bogle, Dalio, Simons, and Soros are **situational lenses**, applied when the question involves their domain (see the Procedure). Source books are in the workspace root and articles/papers in `Publications/`; each reference file links its source.

Detailed rules, thresholds, and examples:
- [Graham reference](./references/Investors/graham.md): margin of safety, defensive/enterprising screens, Mr. Market, allocation, bond coverage
- [Lynch reference](./references/Investors/lynch.md): six categories, perfect-stock traits, P/E vs growth, famous numbers, buy/sell signals
- [Buffett reference](./references/Investors/buffett.md): moats, owner earnings, intrinsic value, capital allocation, management, accounting
- [Munger reference](./references/Investors/munger.md): investing checklist, three baskets, inversion, scale advantages, 25 tendencies / lollapalooza, incentives, option accounting
- [Icahn reference](./references/Investors/icahn.md): asset-value gaps, activist catalysts, proxy mechanics, greenmail costs, governance red flags, case lessons (Baird & Warner, Saxon fraud trap, Hammermill, Marshall Field, Dan River, TWA operator trap)
- [Bogle reference](./references/Investors/bogle.md): cost arithmetic, tax drag, investor-vs-fund return gap, cost-quartile evidence, adviser evaluation, fund-selection odds, index/ETF/hedge-fund checklist, age-based allocation
- [Dalio reference](./references/Investors/dalio.md): uncorrelated return streams, All Weather/risk parity, max-loss controls, debt-cycle gauge, expected-value betting, synthesis rules, believability-weighted decisions
- [Simons reference](./references/Investors/simons.md): why discretion failed, the 1989 short-term turnaround, statistical edges, overfitting, slippage and capacity, leverage via basket options, model risk (2000, 1998 LTCM, 2007), quant/backtest evaluation checklist
- [Soros reference](./references/Investors/soros.md): reflexivity, boom/bust stages, conglomerate and REIT equity-leverage arithmetic, credit/collateral loops, fallibility, survival and leverage limits

Publication references (single articles/papers; use alongside the matching investor lens):
- [Graham 1932, return stockholders' cash](./references/Publication/graham-1932-return-cash.md): cash-rich stocks below net current assets, pro-rata repurchase vs open-market buybacks, dividend-before-buyback duty, earnings-watering red flags
- [Buffett 1984, Superinvestors of Graham-and-Doddsville](./references/Publication/buffett-superinvestors-1984.md): skill-vs-luck test for track records, price-vs-value focus, lower price = lower risk, margin-of-safety sizing, size as performance anchor
- [Bogle 2005, relentless rules of humble arithmetic](./references/Publication/bogle-humble-arithmetic-2005.md): Cost Matters Hypothesis, fund vs investor return tables, manager-structure evidence, lifetime cost compounding, pension-return-assumption check
- [Soros 2013, fallibility and reflexivity](./references/Publication/soros-fallibility-reflexivity-2013.md): near- vs far-from-equilibrium, boom-bust stages AB-HI, price-to-fundamentals pathways, conjecture-vs-price trading discipline, fat tails
- [Dalio 2017, productivity and structural reform](./references/Publication/dalio-productivity-structural-reform-2017.md): country growth formula (productivity 2/3, indebtedness 1/3), gauge weights and correlations, country life cycle, 2017 10-year projections (dated)
- [Chern-Simons 1974](./references/Publication/chern-simons-1974.md): pure mathematics; Simons background only, no investing rules

Accounting references (how the reported numbers are built; synthesized from three financial-accounting textbooks in `Books/Accounting Books/`):
- [Accounting foundations](./references/Accounting/accounting-foundations.md): GAAP/IFRS principles, accruals and omission effects, statement links, classified balance sheet, notes, audit opinion, GAAP-vs-IFRS differences
- [Revenue and receivables](./references/Accounting/revenue-receivables.md): recognition criteria, long-term contracts, revenue fraud schemes, bad-debt methods, DSO, earnings-management levers
- [Inventory and COGS](./references/Accounting/inventory-cogs.md): FIFO/LIFO/average effects, LCM/LCNRV, two-period inventory errors, count rules, turnover and days in inventory
- [Long-lived assets and investments](./references/Accounting/long-lived-assets-investments.md): capitalize vs expense, depreciation estimates, impairment, disposal gains, intangibles, goodwill, equity-method and fair-value investments
- [Liabilities and debt](./references/Accounting/liabilities-debt.md): current vs long-term, contingencies matrix, warranties, loans, bond pricing and effective interest, covenants, debt-like items
- [Equity and EPS](./references/Accounting/equity-eps.md): preferred and arrears, treasury stock and buybacks, dividends, splits, restatements/OCI, book value per share, EPS normalization
- [Cash flow statement](./references/Accounting/cash-flow-statement.md): classification (GAAP vs IFRS), indirect/direct method, free cash flow, cash-flow patterns, distortion points
- [Ratio analysis](./references/Accounting/ratio-analysis.md): liquidity, profitability, leverage, market ratios with worked examples; horizontal/vertical/common-size; DuPont; formula quick reference
- [Red flags and forensics](./references/Accounting/red-flags-forensics.md): fraud triangle, case library (Enron, WorldCom, HealthSouth, Waste Management, Lehman), red-flag matrix by statement area, forensic workflow

When a publication note exists for the question at hand, use it before the longer book summary for the same lens.
There is no separate publication note in this repo for Bogle or Icahn; use the book summary plus the underlying fund filings, annual reports, proxy materials, 13D filings, and issuer disclosures.

**Foreign securities:** state the reporting currency and filing framework (GAAP vs IFRS vs local GAAP) up front. Local accounting standards can differ materially from US GAAP (e.g., revenue recognition timing, lease treatment, goodwill amortization); flag any ratio that isn't directly comparable to a US peer without adjustment. Do not silently convert or mix currencies — show the FX rate and date used for any cross-currency comparison.

**Calculations:** use `scripts/valuation_calcs.py` for every formula below instead of deriving it by hand — it is tested against the worked examples cited in the reference docs (run `python scripts/test_valuation_calcs.py` to verify). Available: `graham_number`, `graham_growth_value`, `ncav_per_share`, `earnings_yield`, `margin_of_safety`, `peg_ratio`, `dividend_adjusted_ratio`, `net_cash_per_share`, `pe_ex_cash`, `owner_earnings`, `owner_earnings_dcf` (plus `owner_earnings_dcf_range` for low/base/high sensitivity), `dollar_test`. Run `python scripts/valuation_calcs.py <command> --help` for arguments, or import the functions directly. All percentage inputs are whole numbers (`12` for 12%, not `0.12`).

## Operating Rules

- **Separate facts, estimates, and judgments.** Give each factual number a source and period. Label analyst estimates, user assumptions, and your own calculations separately.
- **Use point-in-time data.** State the price timestamp, reporting currency, latest filing period, and fiscal year-end. Do not combine a current price with stale shares, debt, cash, or earnings without warning.
- **Prefer primary evidence.** Use audited annual filings, interim filings, proxy statements, and investor-relations releases before aggregators or commentary. Cite the exact filing and period when tools provide it.
- **Adjust before valuing.** Reconcile diluted shares, stock-based compensation, leases, pensions, minority interests, acquisitions, discontinued operations, and recurring "one-time" charges when material.
- **Do not force every lens.** Apply only methods suited to the business and available evidence. Mark a lens `Not applicable` with one reason rather than manufacturing a score.
- **Use ranges, not point precision.** Show assumptions and sensitivity. A precise output from uncertain inputs is not a precise valuation.
- **Stop when evidence is inadequate.** Return `Insufficient data` or `Too hard` instead of a Buy/Hold/Sell verdict when value depends on unavailable, stale, or unreliable inputs.

## Shared Core Principles

1. **A stock is part-ownership of a business.** Analyze the business, not the ticker chart.
2. **Margin of safety.** Pay well below a conservative value estimate; the gap absorbs errors and bad luck.
3. **Mr. Market serves you, he doesn't guide you.** Price swings create opportunities; never let quotes dictate your judgment.
4. **Stay within your circle of competence / your edge.** Knowing the circle's boundaries matters more than its size.
5. **Long horizon.** Earnings drive price over 3–10+ years; short-term moves are noise. Market timing and macro forecasting don't work.
6. **Costs, turnover, and taxes destroy returns.** Low-cost index funds beat most professionals for people who won't do the work.
7. **Avoid speculation disguised as investment:** hot IPOs, story stocks without earnings, options/futures, shorting, leverage on margin.
8. **Invert and check incentives.** Ask what would make this fail, and who profits from the recommendation (Munger).
9. **Survive first.** Diversify across truly uncorrelated drivers and cap the loss any single bet can cause (Dalio, Simons).

## Procedure

### Step 1: Clarify the task and the investor
- Identify request type: single-stock analysis, valuation, screen, buy/sell/hold decision, portfolio review, fund/ETF comparison, special situation (asset play, activist, spin-off), quant/backtest evaluation, or behavior check.
- Choose lenses: Graham, Lynch, Buffett, and Munger for every stock. Add Icahn for asset-value gaps, governance, and catalysts. Add Bogle for funds, costs, and the passive-vs-active choice. Add Dalio for portfolio risk, correlation, and macro/debt exposure. Add Simons for systematic or backtested strategies. Add Soros for suspected bubbles, acquisition- or issuance-driven EPS growth, and credit-fueled sectors.
- Determine investor type (Graham): **defensive** (little time, wants safety → index funds or strict Ch. 14 screen) vs **enterprising** (will do serious research → bargains, Lynch/Buffett-style picks).
- For personalized portfolio or suitability questions, ask for jurisdiction, account type, time horizon, liquidity needs, emergency reserve, debt, tax constraints, loss tolerance, current holdings, and position sizes. If these are missing, keep the answer general.
- Readiness check (Lynch): emergency money set aside and only invest money not needed for several years. Treat his "own a home first" view as a historical heuristic, not a universal requirement.

### Step 2: Gather data (never invent numbers)
Collect what is available; state explicitly which items are missing or estimated. If the user hasn't provided data and no tool can fetch it, ask for it or proceed with clearly labeled assumptions.

Use the [Accounting references](./references/Accounting/accounting-foundations.md) to normalize reported figures (non-operating gains, estimate changes, classification choices) and to run the [ratio workflow](./references/Accounting/ratio-analysis.md) and [forensic checks](./references/Accounting/red-flags-forensics.md) before valuing.

Start with a **data snapshot**: company/security, exchange, currency, price and timestamp, market-cap date, latest filing and period, fiscal year-end, and sources. For ADRs, funds, dual listings, or multiple share classes, verify the security, ratio, and share class before calculating per-share values.

| Area | Items |
|------|-------|
| Price | Share price and timestamp, basic and diluted shares, options/RSUs/convertibles, market cap |
| Earnings | EPS for 10 years (min 5), 3-yr average EPS, expected growth 5–10 yrs |
| Balance sheet | Current assets, current liabilities, cash, long-term debt (bank vs funded), equity, tangible book, inventories, receivables, pension status |
| Cash flow | Operating cash flow, D&A, stock-based compensation, capex (maintenance vs growth), working-capital needs, free cash flow |
| Returns | ROE, ROIC, pretax margin (10-yr trend) |
| Shareholder | Dividend history and payout ratio, buybacks vs dilution, insider buying/selling, institutional ownership, analyst coverage |
| Business | What it sells, % of sales/profits from key product, competitors, pricing power, reinvestment needs, management record |

### Step 3: Graham lens (quantitative safety)
- Run the **defensive** 7-criteria screen or the **enterprising** 5-criteria screen (see [graham.md](./references/Investors/graham.md)).
- For cash-rich, payout, or buyback questions, cross-check [Graham 1932](./references/Publication/graham-1932-return-cash.md) first.
- Compute:
  - P/E on 3-yr average earnings (defensive limit ≤ 15)
  - P/B (≤ 1.5) and **P/E × P/B ≤ 22.5** → derived **Graham Number** = $\sqrt{22.5 \times \text{EPS}_{3yr\,avg} \times \text{BVPS}}$. Do not calculate it when average EPS or BVPS is non-positive.
  - Net current asset value (NCAV) = current assets − all liabilities − preferred; net-net if price < NCAV per share (stricter classic rule: ≤ 2/3 NCAV)
  - Price vs tangible book: conservative buyers stay within ~1/3 above tangible asset value (Ch. 8)
  - Earnings yield vs high-grade bond yield (Ch. 20 margin of safety)
  - Optional growth formula: $V = E \times (8.5 + 2g)$, g = expected 7–10 yr growth %. Graham warns this is illustrative and can overstate value; never rely on it alone.
- Flag speculative elements: P/E far above 25× 7-yr avg earnings, no earnings record, heavy debt, hype.

### Step 4: Lynch lens (category + story)
- Classify into one of six categories: **slow grower, stalwart, fast grower, cyclical, turnaround, asset play** (see [lynch.md](./references/Investors/lynch.md)). Category determines expectations, what to check, and when to sell.
- Write the **two-minute story**: why it will grow, what must go right, what could go wrong.
- Compute:
  - P/E ÷ growth (PEG): ≈1 fair, ≈0.5 very attractive, ≥2 very unattractive. Enter growth as a whole percentage (for example, `15`, not `0.15`), use a defensible forward or normalized rate, and do not use PEG for negative or highly cyclical earnings.
  - Dividend-adjusted: $(g + \text{yield}) / \text{P/E}$ → <1 poor, 1.5 okay, ≥2 good
  - Net cash per share; P/E ex-cash = (Price − net cash/share) ÷ EPS
  - Debt/equity (normal ≈ 25/75), bank vs funded debt
  - Inventory growth vs sales growth (red flag if inventory grows faster)
  - Free cash flow per share
- Assess the 13 perfect-stock traits and the "stocks to avoid" list; do not collapse qualitative evidence into an arbitrary numeric score.

### Step 5: Buffett lens (business quality + owner value)
- **Understandable?** Inside circle of competence? Fast-changing technology → usually "too hard".
- **Durable moat / franchise?** Pricing power, little capital needed, high ROE with little debt, consistent earning power. Commodity business → avoid unless lowest-cost producer at a deep discount.
- For track-record, manager-skill, or price-vs-value arguments, cross-check [Buffett 1984](./references/Publication/buffett-superinvestors-1984.md) first.
- **Owner earnings** = net income + D&A and other non-cash charges − average maintenance capex (− extra working capital needed). Ignore EBITDA.
- **Intrinsic value** = discounted owner earnings over the business's life. Use conservative growth and a discount rate at least equal to the relevant long-term government bond yield plus a safety cushion. Keep cash flows and discount rates consistently nominal or real, cap mature terminal growth below long-run nominal economic growth, include net debt and other senior claims, use diluted shares, and show low/base/high sensitivity.
- **$1 test**: has each $1 retained created ≥ $1 of market value over 5–10 years?
- **Management**: candid reporting, rational capital allocation, buybacks only below intrinsic value, owner-like pay, resistance to the institutional imperative, no empire-building acquisitions.

### Step 6: Munger lens (inversion, incentives, biases)
- **Basket:** yes / no / too tough to understand. If too tough, stop and say so.
- **Invert:** list the ways the investment could cause a permanent loss (competitive destruction, technology passing gains to customers, leverage, fraud, bad incentives).
- **Return-on-capital test:** long-run stock return ≈ the business's return on capital. Is ROIC durably high, with room to reinvest?
- **Incentives:** management pay structure, option dilution (recast earnings with option costs as an expense), advisers' and brokers' commissions.
- **Bias audit:** check both the thesis and the market narrative against the 25 tendencies. Flag lollapalooza setups (several biases pushing one direction, e.g., social proof + envy + authority in a bubble).
- **Opportunity cost:** is this better than the best idea already owned or an index fund? Bet big only when the odds are clearly favorable.

### Step 7: Situational lenses (apply only those that fit)
- **Icahn: asset value and catalyst** (asset plays, conglomerates, poorly governed companies): sum-of-the-parts or liquidation value vs price; why the gap exists; a concrete catalyst (activist 13D, spin-off, sale, buyback); governance red flags (low insider ownership, poison pill, staggered board, dual-class shares, related-party fees, premium buybacks for one holder); accounting quality behind the asset value; downside floor; timeline risk; operator risk in capital-intensive, cyclical, labor-heavy businesses.
- **Bogle: cost and passive default** (funds, ETFs, advisers, "should I pick stocks?"): all-in cost = expense ratio + loads + ~1% × turnover + cash drag + taxes; the odds of active outperformance; reversion to the mean in past winners; the index fund as the default benchmark; Funny Money ≤ 5%. Also check tax drag in taxable accounts, the hot-fund behavior gap (investor return vs fund return), and adviser fees (fee-only, ≤ 1%).
- **Dalio: portfolio risk** (portfolio reviews, macro worries): count independent return streams (correlation, not tickers); coverage across growth up/down × inflation up/down; max loss per bet or correlated cluster; debt-service vs cash flow and rates near zero; a backup plan if wrong. Also frame the thesis as an expected-value bet (probability × payoff, both sides) and ask what the consensus price already assumes; consider not betting at all when confidence is low; look for hidden currency or rate speculation.
- For country growth, debt-cycle, or long-run growth assumptions, cross-check [Dalio 2017](./references/Publication/dalio-productivity-structural-reform-2017.md) first.
- **Simons: systematic strategies** (quant funds, backtests, trading systems): out-of-sample record, plausible mechanism, independent sample size, overfitting controls, costs and capacity, leverage and crowding, automatic risk reduction, signal decay, fee share, whether the buyable fund is the one with the record. Default to an index fund absent a verifiable edge.
- The Chern-Simons paper is background only; do not use it for investing claims. Use [Simons 1974 background](./references/Publication/chern-simons-1974.md) only to understand his academic history.
- **Soros: reflexivity and boom/bust** (hot sectors, serial acquirers, companies issuing stock at a premium, lenders to a booming market): is the share price or new credit feeding the fundamentals? Separate organic EPS growth from growth bought with expensive paper. Name the flawed perception and the boom/bust stage (early, tested, late). Late-stage signs: scarce corrections, easy entry, rising leverage, creative accounting. Busts are sudden; size positions so being wrong is survivable. If no feedback loop is visible, skip this lens.
- For reflexivity, boom-bust staging, and leverage-fed fundamentals, cross-check [Soros 2013](./references/Publication/soros-fallibility-reflexivity-2013.md) first.

### Step 8: Reconcile and decide
- Build a value range from the methods that fit the category (e.g., Graham number/NCAV for asset plays and slow growers; PEG + owner-earnings DCF for stalwarts and fast growers; normalized mid-cycle earnings for cyclicals; survival + recovery earnings for turnarounds).
- **Margin of safety** = (conservative value − price) ÷ conservative value. Guidelines: defensive ≥ 25–33%; secondary/less-proven companies ≥ 33%; wonderful businesses may be bought at a "fair" price if the moat is durable.
- Where frameworks disagree, say so explicitly (e.g., Graham fails it on P/B but Buffett/Lynch like the franchise).
- State what the current price appears to imply about growth, margins, or returns on capital; compare that expectation with the evidence.
- Assign confidence: **High / Medium / Low**, based on data quality, business predictability, valuation-method agreement, and sensitivity to key assumptions.
- Verdict: **Buy / Accumulate below $X / Watch / Hold / Trim / Sell / Avoid / Too hard / Insufficient data**, with key reasons and what would change the view. For users who do not already own the security, do not use `Hold`; say `Watch` or `Avoid`.
- For holdings: apply category-specific sell signals (Lynch) and "story intact?" test. Never sell just because price fell; never buy just because price fell.

### Step 9: Portfolio-level checks (when relevant)
- Graham allocation: 25–75% stocks, default 50/50; rebalance when drift ≥ 5 pts (or every 6 months, per Zweig). Bogle alternative: bonds ≈ your age (or age − 10); international ≤ ~20% of equities.
- Diversification:
  - Graham defensive investor: 10–30 stocks.
  - Lynch small investor: 3–10 stocks they truly understand.
  - Buffett/Munger "know-something" investor: a few (5–10) great businesses, bet heavily when the odds are favorable.
  - "Know-nothing" investor: index fund with periodic purchases.
  - Dalio: measure diversification by uncorrelated return streams (15–20 ideal for a professional). A thousand 60%-correlated stocks diversify little more than five.
- Lynch category mix; avoid "diworseification" in a portfolio too (owning names you don't follow).
- Costs (Bogle): total all-in fund costs and taxes; flag closet indexers, funds-of-funds, and high-turnover funds.
- Speculative money kept separate: Zweig "mad money" ≤ 10%; Bogle "Funny Money" ≤ 5%.
- Risk (Dalio/Simons/Soros): no single position or correlated cluster can cause an unacceptable loss; check leverage and crowded trades; never run close to margin limits (forced-seller risk).
- Behavior audit: check against Lynch's twelve silliest things, Graham/Zweig behavioral pitfalls, and Munger's 25 tendencies.

## Output Template

```
## [Company] ([Ticker]) at $[price]: [Verdict]

**Category (Lynch):** ...    **Investor fit (Graham):** Defensive / Enterprising / Neither
**Two-minute story:** ...

### Key Numbers
| Metric | Value | Benchmark | Pass? |

**Data snapshot:** price/time, currency, filing period, fiscal year-end, primary sources

### Graham: Safety     (screen results, Graham number, NCAV, earnings yield vs bonds)
### Lynch: Story & Growth (PEG, dividend-adjusted ratio, cash, debt, inventories, traits)
### Buffett: Business Quality (moat, ROE, owner earnings, intrinsic value range, management)
### Munger: Inversion & Incentives (basket, failure modes, ROIC, incentives, bias audit)
### Situational Lenses (only those applied: Icahn catalyst / Bogle cost / Dalio risk / Simons quant / Soros reflexivity)

### Valuation Summary
| Method | Value/share | Notes |
Conservative value: $X  |  Margin of safety: Y%

### Market-Implied Expectations
### Verdict & Confidence

### Risks & Red Flags
### What Would Change My Mind
### Data Gaps / Assumptions
```

## Guardrails

- Educational analysis, not personalized financial advice; say so once, briefly.
- Never fabricate financial data. Label every estimate and its source or assumption.
- Never present old book thresholds, historical examples, or historical fund results as current evidence. Preserve the original period and distinguish source doctrine from present-day analysis.
- Do not double-count cash, debt, leases, minority interests, or stock-based compensation across owner earnings, enterprise value, and per-share value.
- For foreign securities, identify currency and translation date; do not mix reporting currency with trading currency silently.
- 1970s/1980s thresholds (Graham's $100M sales, Lynch's dollar examples) must be scaled for inflation and modern markets; state the adjustment used. Zweig's commentary updates are in [graham.md](./references/Investors/graham.md).
- Adapt for sector: banks/insurers/REITs/utilities don't fit current-ratio tests; use sector-appropriate measures (book value, coverage, combined ratio, FFO).
- Prefer normalized multi-year earnings over a single year; strip out one-time items, but treat recurring "one-time" charges as normal costs.
- Don't predict short-term prices, the market, interest rates, or the economy. Dalio's debt-cycle gauge is for risk balancing, not market timing.
- Activist tactics (Icahn), quant trading (Simons), and leveraged macro speculation (Soros) need capital, data, and infrastructure individuals lack. Apply their *analysis*, not their *tactics*.
- Soros's reflexivity lens flags boom/bust risk; it is not a market-timing tool. He says turning points can't be determined until they occur, and his own crash and recession calls were often wrong.
