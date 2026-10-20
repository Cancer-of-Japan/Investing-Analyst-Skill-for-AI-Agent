# Financial Statement Analysis: Ratios, Trend and Common-Size Analysis, DuPont

Sources: [LY] Lyryx Ch 12 (main source), App 6A, 7A, 7B; [JN] Jonick Ch 7.3; [OS] OpenStax Appendix A, 5.3, 9.3, 10.5, 14.5, 16.5. Full citations in [accounting-foundations.md](./accounting-foundations.md).

**Ground rules from the books**
- "One of the main purposes of ratio analysis is to highlight areas that require further analysis and investigation. Ratio analysis alone will not provide a definitive financial evaluation??when combined with informed judgment, offers insight" [LY 12.1].
- "no ratio is particularly meaningful by itself; it needs to be compared to something else, such as desired or expected results, previous results, other companies' results, or industry standards" [JN 7.3].
- Compare with **industry averages** and the **company's own history** [LY 12.1]. "Using ratios for a single year does not provide a broad picture" [OS 5.3].
- When a ratio mixes an income-statement flow with a balance-sheet stock, use the **average** of opening and closing balances [LY 12.1 fn 2].
- Qualitative factors can override strong numbers: LY's refrigerator maker with good ratios but a technology shift it cannot make ??"present positive financial indicators may not accurately reflect the likely future" [LY 12.1].
- Limitations: "past performance does not always dictate future performance"; inflation and recessions skew numbers; reporting methods change "which may not be readily evident" [OS App A].

---

## 1. Worked Datasets Used Below

### LY Big Dog Carworks Corp. ($000s) [LY 12.1]

| Balance sheet | 2024 | 2023 | 2022 |
|---|---|---|---|
| Cash | 20 | 30 | 50 |
| Short-term investments | 36 | 31 | 37 |
| AR | 544 | 420 | 257 |
| Inventories | 833 | 503 | 361 |
| **Current assets** | **1,433** | **984** | **705** |
| PP&E, net | 1,053 | 1,128 | 712 |
| **Total assets** | **2,486** | **2,112** | **1,417** |
| Borrowings (current) | 825 | 570 | 100 |
| AP | 382 | 295 | 219 |
| Income tax payable | 48 | 52 | 50 |
| **Total liabilities (all current)** | **1,255** | **917** | **369** |
| **Equity** | **1,231** | **1,195** | **1,048** |

| Income statement | 2024 | 2023 | 2022 |
|---|---|---|---|
| Net sales | 3,200 | 2,800 | 2,340 |
| COGS | 2,500 | 2,150 | 1,800 |
| Gross profit | 700 | 650 | 540 |
| Operating expenses | 400 | 376 | 336 |
| **Income from operations** | **300** | **274** | **204** |
| Interest | 89 | 61 | 0 |
| Income tax | 95 | 96 | 92 |
| **Net income** | **116** | **117** | **112** |
| Dividends declared | 80 | 70 | 60 |

100,000 common shares outstanding each year-end; assumed average prices $6 / $5 / $4.

### JN Jonick Company 2019 (2018) [JN 7.3]
Sales $994,000 ($828,000); COGS 414,000 (393,000); gross profit 580,000 (435,000); operating expenses ??48,000 (290,000); **income from operations 232,000 (145,000)**; gain on sale of investments **137,000** (186,000); interest 55,000 (50,000); pretax 314,000 (281,000); tax 66,000; **net income 248,000 (231,000)**; preferred dividends 12,000; common dividends 8,000. Current assets 911,000; current liabilities 364,000; total assets 3,950,000 (3,606,000) incl. long-term equity securities 1,946,000 (1,822,000); long-term liabilities 911,000; total liabilities 1,275,000; equity 2,675,000 (2,447,000); 8,300 common shares; price $70.

### OS Banyan Goods [OS App A]
Net sales $120,000; credit sales $100,000; COGS $60,000; EBIT $43,000; interest $2,000; net income $35,000; current assets $200,000 (cash 110,000; short-term investments 20,000; AR 30,000; inventory 40,000); current liabilities $100,000; total assets $250,000 (prior $200,000); liabilities $150,000; equity $100,000 (prior $90,000); AR prior $20,000; inventory prior $35,000.

---

## 2. Liquidity Ratios

| Ratio | Formula | Examples | Book interpretation |
|---|---|---|---|
| **Working capital** | CA ??CL | Big Dog $336 ??$67 ??$178; Banyan $100,000; Printing Plus $21,140 [OS 5.3] | "too large of a difference may indicate that the company may not be correctly using their assets" [OS App A] |
| **Current ratio** | CA ÷ CL | Big Dog 1.91 ??1.07 ??1.14; Jonick 2.5; Banyan 2.0; Printing Plus 4.91 | See benchmarks below |
| **Quick (acid-test)** | (Cash + short-term investments + receivables) ÷ CL; excludes inventory ("two steps from cash") and prepaids [LY App 7A] | Big Dog 0.93 ??0.52 ??0.48; Jonick 2.0; Banyan 1.6 | "a 1:1 acid test ratio is adequate??However, this is a fairly arbitrary guideline??A lower ratio than 1:1 can often be found in successful companies" [LY 12.2] |
| **AR turnover** | Net credit sales ÷ Average AR | Jonick 10.0; Banyan 4; BWW 5.14 | Higher is better [JN; LY App 7B] |
| **Days' sales in receivables / collection period** | Average AR ÷ net credit sales ? 365 | Big Dog 44.13 ??54.98 days (terms net 30); Jonick 36.5 | Lower is better; compare with credit terms |
| **Inventory turnover** | COGS ÷ Average inventory | Jonick 8.0; Banyan 1.6 ("very low"); LY A 5? vs B 2.5? | Higher is better |
| **Days' sales in inventory** | Average inventory ÷ COGS ? 365 | Big Dog 73.34 ??97.53; Jonick 45.4; Banyan 243 ("unsustainable") | Lower is better, unless deliberate stock-up |
| **Revenue operating cycle** | DSI + collection days | Big Dog 117.47 ??152.51 days | If AP terms are 60 days, Big Dog "may not be able to pay them" [LY 12.2] |

**Current ratio benchmarks**
- "Some analysts consider that a corporation should maintain a 2:1 current ratio, depending on the industry??no one current ratio is applicable to all entities" [LY 12.2].
- OS 5.3 ranges: many companies 1.5???; utilities 1.25??.5?; high-tech start-ups 2.5???.
- Too high can be bad: LY's Company C with acid-test 8.7 has "idle assets" [LY App 7A]. JN: a debt-tolerant company "may consider 2.5 to be too high" [JN 7.3.4].
- **Composition matters** [LY 12.2]: Corp A and B both at 2:1, but A's current assets are $37,000 of $40,000 inventory while B's are mostly cash and receivables. B is safer; A would have to sell inventory "likely at a lower?�than?�normal gross profit." The current ratio "is only a rough indicator."
- Graham's industrial screen asks for current ratio ??2 and net current assets ??long-term debt (see [graham.md](../Investors/graham.md)); these books show why composition and trend must be checked too.

**LY's liquidity conclusion on Big Dog:** "it appears that Big Dog Carworks Corp. is growing less liquid. Current assets, especially quick assets, are declining relative to current liabilities. The revenue operating cycle is increasing."

---

## 3. Profitability Ratios

| Ratio | Formula | Examples | Notes |
|---|---|---|---|
| **Gross profit ratio** | Gross profit ÷ Net sales | Big Dog 23.08% ??23.21% ??21.88%; Jonick 58.4% | "even a small decline in this percentage can affect net income significantly" [LY 12.3] |
| **Operating profit ratio** | Income from operations ÷ Net sales | Big Dog 8.72% ??9.79% ??9.38%; Jonick 23.3% | Leaves room for interest and tax |
| **Net profit margin** | Net income ÷ Net sales | Big Dog 4.79% ??4.18% ??3.63%; Jonick 24.9%; Banyan 29% | "what percentage of sales are left over after all expenses are paid" [JN] |
| **Asset turnover (sales to total assets)** | Net sales ÷ Average total assets | Big Dog 1.59 ??1.39; Banyan 0.53 | JN **excludes long-term investments** ("not productivity assets"): Jonick 52.5% |
| **Return on assets** | See variants below | Big Dog 15.53% ??13.05%; Jonick 8.0%; Banyan 16% | Higher is better |
| **Return on equity** | Net income ÷ Average equity | Big Dog 10.43% ??9.56%; Jonick 9.7%; Banyan 37% | |
| **Return on common equity** | (NI ??Preferred dividends) ÷ Average common equity | Jonick 9.9% ("every dollar??earned about $.10") | Common equity excludes preferred [JN] |

### ROA has three textbook definitions ??state which one you use

| Book | Numerator | Rationale | Example |
|---|---|---|---|
| LY | **Income from operations** (pre-interest, pre-tax) | "all the assets of the company are considered in the ratio's denominator, whether financed by investors or creditors" | Big Dog 2024: 300 ÷ 2,299 = 13.05% |
| JN | **Net income + interest expense** (not tax-adjusted) | "how the assets are paid for should be irrelevant" | Jonick: (248,000 + 55,000) ÷ 3,778,000 = 8.0% |
| OS | **Net income** | Simple | Banyan: 35,000 ÷ 225,000 = 16% |

[Analyst preference for business-quality comparisons: after-tax operating income (NOPAT) ÷ invested capital (ROIC), as used in the Buffett and Munger lenses. The LY definition is the closest of the three to a pre-tax ROIC.]

### LY's observations on Big Dog profitability
- Sales grew but net income did not; "Their increasing operating expenses appear to be an issue" ??later reversed by trend analysis (Section 6), which shows COGS, not operating expenses, rising as a share of sales.
- Asset turnover and ROA fell because "Income from operations has not increased with the growth in the asset base"; it may be too early to judge the new PP&E.
- [Derived] Effective tax rate ??5% each year; ROE (9.6%) below operating ROA (13%) because of interest and tax.

---

## 4. Leverage and Coverage Ratios

| Ratio | Formula | Examples | Interpretation |
|---|---|---|---|
| **Debt ratio** | Total liabilities ÷ Total assets | Big Dog 26% ??43.42% ??50.48% | "Generally, this is considered an unfavourable trend??The greater the debt financing, the greater the risk" [LY 12.4] |
| **Equity ratio** | Total equity ÷ Total assets | Big Dog 56.58% ??49.52% | Debt ratio + equity ratio = 100% |
| **Debt-to-equity** | Total liabilities ÷ Total equity | Big Dog 0.35 ??0.77 ??1.02; Jonick 0.48 (book prints "5", an error); Banyan 1.5 | "there is no single most appropriate debt to equity ratio" [LY]; Banyan's 1.5 "could be a red flag??trending toward insolvency" [OS]; JN: depends on tolerance for debt |
| **Times interest earned** | Income from operations ÷ Interest [LY; OS] ??or (Pretax income + interest) ÷ interest [JN] | Big Dog 4.49 ??3.37; Banyan 21.5; Jonick 6.7 | "The larger the ratio, the better creditors are protected" [LY] |
| **Fixed assets to long-term liabilities** | Net PP&E ÷ LT liabilities | Jonick 1.2 | Higher is better [JN] |
| **Times preferred dividends earned** | Net income ÷ Preferred dividends | Jonick 20.7 | Higher is better [JN] |

**Caution on JN's coverage:** Jonick's pretax income includes the $137,000 investment gain. On operating income only, coverage is 232,000 ÷ 55,000 ??**4.2?**, not 6.7? [derived]. Use operating income (EBIT) for coverage.

**Pros and cons of creditor financing** [LY 12.4]: no dilution of control and positive leverage if borrowed funds earn more than their interest cost; but interest and principal are mandatory and rising rates hit earnings. "From the creditors' perspective, the more capital invested by owners of the company, the greater the relative risk assumed by shareholders thus decreasing risk to creditors."

See [liabilities-debt.md](./liabilities-debt.md) for covenants, maturities, and debt-like items.

---

## 5. Market Ratios

| Ratio | Formula | Examples |
|---|---|---|
| **EPS** | (NI ??Preferred dividends) ÷ Weighted average common shares | Big Dog $1.12 ??$1.17 ??$1.16; Jonick $28.43 |
| **P/E** | Price ÷ EPS | Big Dog 3.57 ??4.27 ??5.17; Jonick 2.5 |
| **Earnings yield** [derived] | EPS ÷ Price | Big Dog 28.0% ??23.4% ??19.3% |
| **Dividends per share** | Common dividends ÷ Common shares | Big Dog $0.60 ??$0.80; Jonick $0.96 |
| **Dividend yield** | DPS ÷ Price | Big Dog 15% ??14% ??13%; Jonick 1.4% |
| **Payout ratio** [derived; not defined in the books] | Dividends ÷ Net income | Big Dog 53.6% ??59.8% ??69.0% |
| **Book value per common share** | (Equity ??preferred claims) ÷ Common shares [LY 10.5] | Big Dog $10.48 ??$11.95 ??$12.31 [derived] |
| **Price-to-book** [derived] | Price ÷ BVPS | Big Dog 0.38 ??0.42 ??0.49 |

- LY: the share price "is perhaps the most important measure of a company's financial performance"; P/E is "an indicator of the market's expectation of a company's future performance." Big Dog's rising P/E means investors are "bullish" despite flat EPS.
- LY red flag: rising dividends despite flat income and poor liquidity ??"Investors might ask why such high levels of dividends are being paid given this situation."
- **Value-investing caution:** JN states P/E "The higher the better" [JN 7.3.4]. That reflects market optimism, not value. For Graham/Lynch/Buffett, compare P/E with growth (PEG), normalized earnings, and bond yields; a low P/E with durable earnings is the opportunity. Big Dog's P/E of ~5 and P/B ~0.5 would look statistically cheap, but its liquidity problems are exactly the kind of risk that keeps such stocks cheap ??check balance-sheet safety before buying cheapness.

Details on EPS, buybacks and book value: [equity-eps.md](./equity-eps.md).

---

## 6. Horizontal, Vertical, and Common-Size Analysis

### Definitions
- **Horizontal (trend) analysis:** % change vs a base year (usually the oldest = 100%) or year-over-year. Change = Current ??Base; % change = Change ÷ Base [LY 12.7; JN 7.3.1; OS App A].
- **Vertical analysis:** each line as % of a base ??**sales** for the income statement, **total assets** (= total liabilities + equity) for the balance sheet [LY 12.7; JN 7.3.2; OS App A].
- **Common-size statements:** statements showing only these percentages, used to compare companies of different size or against industry averages [JN 7.3.3].
- LY: "The percentage change must always be interpreted together with the absolute dollar amount of change to avoid incorrect conclusions; percentage can sometimes be misleading."
- OS: "If multiple periods are not used, it can be difficult to identify a trend."

### LY Big Dog 2024 vs 2023

| | % change | Common-size 2024 | Common-size 2023 |
|---|---|---|---|
| Sales | +14% | 100 | 100 |
| COGS | **+16%** | **78** | 77 |
| Gross profit | +8% | 22 | 23 |
| Expenses (operating + interest + tax) | +10% | 18 | 19 |
| Net income | ??% | 4 | 4 |
| Current assets | +45.6% | 57.6% of assets | 46.6% |
| Current liabilities | +36.9% | 50.5% | 43.4% |
| Equity | +3.0% | 49.5% | 56.6% |

**The key reversal** (verbatim): "Initially, it was stated that operating expenses were increasing??Based on trend analysis, however, these expenses are actually declining as a percentage of sales??Conversely, the increases each year in cost of goods sold may be worrisome??(78% vs. 77% of sales) may warrant further investigation." **Ratio conclusions can flip once you look at proportions; always do both.**

Common-size balance sheet: asset mix shifted toward current assets; financing shifted "from equity financing to debt financing."

### JN Jonick 2019 vs 2018

| Line | % change | % of sales 2019 | % of sales 2018 |
|---|---|---|---|
| Sales | +20.0% | 100 | 100 |
| COGS | +5.3% | 41.6 | 47.5 |
| Gross profit | +33.3% | 58.4 | 52.5 |
| Operating expenses | +20.0% | 35.0 | 35.0 |
| **Income from operations** | **+60.0%** | **23.3** | **17.5** |
| Gain on investments | ??6.3% | 13.8 | 22.5 |
| **Net income** | **+7.4%** | **24.9** | **27.9** |

JN: "sales increased 20.0% ??yet gross profit and income from operations increased quite a bit more at 33.3% and 60.0% ??However, the final net income amount increased only 7.4%. Changes between the income from operations and net income lines can be reviewed to identify the reasons." **Operations improved sharply; the bottom line lagged because non-operating gains fell and tax rose.** A value investor should value the operating trend, not the net-income trend.

Balance sheet: total assets +9.5%, liabilities +10.0%, equity +9.3%, "a relatively consistent overall increase"; but AR +18.7% and equipment +107% stand out.

### JN common-size comparison: Jonick vs Schneider [JN 7.3.3]

| | Jonick | Schneider |
|---|---|---|
| Gross profit % | 58.4 | 52.5 |
| Operating income % | 23.3 | 17.5 |
| Investment gains % | 13.8 | 22.5 |
| Net income % | 24.9 | **27.9** |

"Schneider has lower gross profit and net income from operations percentages to sales. Yet Schneider has a higher overall net income due to much greater gains on the sale of investments." **Higher net margin, lower-quality earnings.**

### OS Banyan
Net sales +20%, but AR +50% ??"extending credit more readily than anticipated or not collecting as rapidly." Cash at 44% of assets vs a 40% target suggests reinvesting excess cash.

---

## 7. DuPont Analysis [JN 7.3.4]

$$\text{ROE}=\underbrace{\frac{\text{Net income}}{\text{Sales}}}_{\text{margin}}\times\underbrace{\frac{\text{Sales}}{\text{Average total assets}}}_{\text{turnover}}\times\underbrace{\frac{\text{Total assets}}{\text{Total equity}}}_{\text{leverage}}$$

- JN: two companies with ROE 30%: A = 0.30 ? 0.5 ? 2.0; B = 0.15 ? 4.0 ? 0.5. "Investors are not looking for large or small output numbers from this model. Investors want to analyze and pinpoint what is causing the current ROE." [A leverage factor below 1 is impossible since assets ??equity; treat B as illustrative only.]
- OS Banyan: ROE 37% vs ROA 16% reflects debt-to-equity of 1.5 [derived].
- **Investor rule:** high ROE from margin and turnover is quality (Buffett's "high ROE with little debt"); high ROE from leverage is risk. Big Dog's leverage rose while margin and turnover fell ??ROE held up only because of debt.

---

## 8. LY's Integrated Conclusion on Big Dog (model write-up) [LY 12.6]

1. Sales grow but net income is flat; gross margin roughly constant; costs need scrutiny.
2. Asset turnover and ROA fell after a PP&E expansion; returns have not caught up with the asset base.
3. "**The most immediate problem facing BDCC is the shortage of working capital and its poor liquidity.**" Receivables and inventory grew out of proportion to sales; review credit policy and inventory control.
4. The expansion was financed with short-term borrowings; debt-service capacity and interest coverage are deteriorating "even though it continues to produce net income each year."
5. Remedy: "investigate alternatives to short?�term borrowings, such as converting some of this to long?�term debt and/or issuing additional share capital."
6. Yet the market's rising P/E suggests investors see the problems as temporary.

"Results of ratio analysis are always more useful if accompanied by other information such as overall industry performance, the general economy, financial ratios of prior years, and qualitative factors such as analysts' opinions and management's plans" [LY 12.6].

---

## 9. Ratio Workflow for the Value-Investing Skill

1. **Normalize inputs first:** remove non-operating gains/losses, discontinued operations, and one-offs (keeping recurring "one-time" items); use averages for flow/stock ratios; restate per-share data for splits.
2. **Liquidity:** current and quick ratios with composition; DSO vs credit terms; DSI; operating cycle; trend.
3. **Solvency:** debt ratio, D/E, interest coverage on operating income, debt maturity vs CFO.
4. **Profitability:** gross, operating, net margins; ROA (state definition); ROE decomposed by DuPont; ROIC if data allow.
5. **Efficiency:** asset turnover (excluding non-operating investments), AR and inventory turnover.
6. **Trend and common-size:** at least 3?? years; % change *and* dollar change; check line items growing faster than sales (AR, inventory, COGS, SG&A).
7. **Market:** P/E on normalized EPS, earnings yield vs bond yield, P/B and P/tangible book, dividend yield and payout vs FCF.
8. **Cross-check with cash:** CFO/NI and FCF (see [cash-flow-statement.md](./cash-flow-statement.md)).
9. **Write the story:** like LY 12.6, state the one or two problems that matter most and what management must do; then feed the findings into the Graham/Lynch/Buffett/Munger lenses.

### Formula quick reference

| Ratio | Formula |
|---|---|
| Working capital | CA ??CL |
| Current | CA ÷ CL |
| Quick | (Cash + ST investments + AR) ÷ CL |
| AR turnover | Net credit sales ÷ Avg AR |
| DSO | Avg AR ÷ Sales ? 365 |
| Inventory turnover | COGS ÷ Avg inventory |
| DSI | Avg inventory ÷ COGS ? 365 |
| Operating cycle | DSO + DSI |
| Gross margin | GP ÷ Sales |
| Operating margin | Operating income ÷ Sales |
| Net margin | NI ÷ Sales |
| Asset turnover | Sales ÷ Avg total assets (optionally excluding LT investments) |
| ROA | Operating income, NI + interest, or NI ÷ Avg total assets (state which) |
| ROE | NI ÷ Avg equity |
| Return on common equity | (NI ??Pref. div.) ÷ Avg common equity |
| Debt ratio | TL ÷ TA |
| Debt-to-equity | TL ÷ TE |
| Times interest earned | EBIT ÷ Interest |
| EPS | (NI ??Pref. div.) ÷ Weighted avg common shares |
| P/E | Price ÷ EPS |
| Dividend yield | DPS ÷ Price |
| Payout | Dividends ÷ NI |
| BVPS | (Equity ??preferred claims) ÷ Common shares |
| FCF | CFO ??Capex (OS also subtracts dividends) |
| DuPont | Margin ? Turnover ? Assets/Equity |
