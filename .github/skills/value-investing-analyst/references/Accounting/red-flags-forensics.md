# Red Flags and Forensic Accounting Checklist

Sources: [OS] OpenStax Ch 8, 9.4, 10, 11, 12.3, 14, 16; [LY] Lyryx Ch 4, 7, 11–12; [JN] Jonick Ch 2–7. Full citations in [accounting-foundations.md](./accounting-foundations.md).

Use this file for the Munger inversion step ("what would make this a permanent loss?") and for Buffett's accounting-quality check. It consolidates every warning sign in the three books, with the statement footprint and the test to run.

---

## 1. Why Fraud Happens: the Fraud Triangle [OS 8.1]

Fraud is "the act of intentionally deceiving a person or organization or misrepresenting a relationship in order to secure some type of benefit, either financial or nonfinancial." Criminologist Donald Cressey's triangle:

| Element | Meaning | What an outside investor can observe |
|---|---|---|
| **Incentive / pressure** | Financial or work pressure, greed, wanting to appear successful | Pay tied to EPS or stock price; debt covenants near breach; promised growth targets; equity raises or acquisitions pending; insider selling |
| **Perceived opportunity** | Weak or overridable controls | Dominant CEO/CFO; weak or non-independent audit committee; auditor also selling consulting; material weaknesses; frequent auditor or CFO changes |
| **Rationalization** | Self-justification | Hard to see; aggressive tone toward short sellers, critics, or auditors is a proxy |

"Typically, all three elements of the triangle must be in place" [OS 8.1].

**Financial statement fraud** "occurs when the financial statements are used to conceal the actual financial condition of a company or to hide specific transactions that may be illegal" [OS 8.7]. Motives: obtaining money from investors or lenders; hiding looting ("excessive retirement perks of top executives, unpaid loans to top executives, improper stock options"); driving up the stock price [OS 8.7].

**Earnings management vs manipulation** [OS 9.4]: management "works within GAAP constraints"; manipulation "typically ignores GAAP rules… Carried to an extreme, manipulation can lead to fraudulent behavior." "The major problem… is the engineering of the short-term financial operating decisions." Motives include management bonuses, meeting expectations, raising borrowing capacity, and boosting a sale price [OS 9.4].

---

## 2. Case Library from the Books

| Case | What happened | Lesson / footprint | Source |
|---|---|---|---|
| **Enron** | Booked projected construction profits immediately; moved losing assets to off-balance-sheet special purpose entities; inadequate disclosure; auditor Arthur Andersen also consulted. $40B shareholder loss; stock $91 → <$1 | Off-balance-sheet vehicles, auditor independence, revenue recognized before cash; Beneish M-Score flagged it a year early | OS 8.2, 8.7, 9.4 |
| **WorldCom** | Capitalized costs that should have been expensed; largest Chapter 11 to that date | Capex growing faster than revenue; CFO inflated (outflows moved to investing) | OS 11.2 |
| **HealthSouth** (1996–2002) | False revenue, misstated receivables, misclassified expenses and asset purchases, fraudulent M&A accounting; management override; whole accounting department colluded | Receivables vs revenue; segregation of duties | OS 8.7 |
| **Waste Management** | Altered depreciation estimates (lives/salvage) to overstate net income by $1.7B | Implied asset lives lengthening; low depreciation/gross PP&E vs peers | OS 11.3 |
| **Lehman Brothers** | ~$639B assets vs $613B liabilities, rising net income ($3.1B→$4.1B), $7.2B cash, yet failed in 2008; large negative FCF; couldn't sell assets at book value | Book solvency ≠ liquidity; short-term funding of illiquid assets; negative FCF despite profits | OS 5.3, 16.5 |
| **Bernie Madoff** | Investment fraud of tens of billions; uncovered by analyst Harry Markopolos because returns were abnormally high and steady for years | Implausibly smooth returns | OS 1.4, 8.1 |
| **SCICAP Credit Union** | $2.7M stolen over 37 years; two sets of books; employee never took vacation and had sole password access | Concentration of control | OS 8.1 |
| **Ernst Currier, Security National Bank** | 61 fraudulent loans (~$6.2M) using real and fictitious identities | No segregation of duties | OS 8.2 |
| **GE / Baker Hughes** | Acquisition growth with inadequate due diligence; sellers present the rosiest picture | Acquired earnings quality | OS 9.4 |
| **Equifax 2017** | Data breach of 143M people as an internal-control failure | Operational control risk | OS 8.2 |
| **Big Dog Carworks** (textbook) | Profitable each year but liquidity deteriorating; long-term assets funded with short-term debt; dividends rising | Profit ≠ solvency | LY 12 |
| **Wellbourn** (textbook) | NI $80,500, CFO −$26,200, bonds issued partly to fund $50,000 dividends | Debt-funded dividends | LY 11.3 |
| **Jonick vs Schneider** (textbook) | Higher net margin from investment gains, weaker operations | Non-operating earnings | JN 7.3.3 |

---

## 3. Red-Flag Matrix by Statement Area

### Revenue and receivables (most common fraud area per OS 8.7)
| Signal | Possible cause | Test | Detail |
|---|---|---|---|
| AR growing faster than sales; rising DSO | Channel stuffing, sham sales, loose credit | AR growth vs sales growth; DSO vs credit terms and peers | [revenue-receivables.md](./revenue-receivables.md) |
| DSO unusually *short* vs industry early in company life | Manipulation (OS: "can signal negative earnings behavior") | Compare to peers | OS 9.4 |
| Quarter-end revenue spikes, Q1 returns | Channel stuffing, cut-off | Quarterly patterns | OS 8.7 |
| Revenue up but inventory not down | Bill-and-hold | Inventory vs COGS | OS 8.7 |
| Lower bad-debt %, wider aging buckets, method switch, re-dated past-due accounts | Earnings management | Allowance ÷ gross AR vs aging; quantify profit effect | OS 9.4 |
| Allowance with leftover debit balance | Past under-reserving | Allowance roll-forward | JN 4.4.2; LY 7.4 |
| Notes receivable from customers rising | Customers can't pay | Note balances vs sales | OS 9.6; JN 4.3 |
| Deferred revenue shrinking while revenue grows | Revenue pulled forward | Deferred revenue trend | OS 12.1 |
| Percentage-of-completion margin revisions | Optimistic cost estimates | Contract assets; margin true-ups | OS 9.5 |

### Inventory and COGS
| Signal | Possible cause | Test | Detail |
|---|---|---|---|
| Inventory growing faster than sales; DSI rising; turnover falling | Obsolescence, overproduction, fictitious inventory | DSI trend; inventory vs sales | [inventory-cogs.md](./inventory-cogs.md) |
| Gross margin jump with inventory build | Overstated ending inventory (profit up one-for-one) | Gross-profit-method estimate of ending inventory | OS 10.4; LY 6.4; JN 4.1.4 |
| Inventory method change | Profit management | Policy note; quantify | OS 10.1; LY 6.2 |
| Large shrinkage or sudden write-downs | Theft, poor control, late recognition | Notes; margin breaks | JN 3.5.1 |
| LIFO layer liquidation | One-time margin boost | LIFO reserve note | [analyst practice] |
| Verbatim OS list: fictitious inventory; count manipulation; sales without purchases; fraudulent inventory capitalization | Fraud | Audit, count disclosures | OS 10.1 |

### Long-lived assets and intangibles
| Signal | Possible cause | Test | Detail |
|---|---|---|---|
| Capex or "other assets" growing faster than revenue | Capitalizing operating costs (WorldCom) | Capex/sales; capex/depreciation; FCF vs CFO | [long-lived-assets-investments.md](./long-lived-assets-investments.md) |
| Depreciation falling relative to gross PP&E | Longer lives/higher salvage (Waste Management) | Implied useful life trend | OS 11.3 |
| Prospective estimate changes boosting profit | Earnings management | PP&E note; quantify | OS 11.5; LY 8.4 |
| Recurring gains on asset sales | Selling fully depreciated assets to lift EPS | Exclude from operating income | OS 11.5 |
| Large capitalized interest or development costs | Profit flattery | Policy note | LY 4.3, 8.1 |
| Goodwill large vs equity; impairments after acquisitions | Overpayment | Goodwill/equity; organic vs acquired growth | OS 11.4 |
| R&D cut while margins rise | Borrowed future earnings | R&D/sales trend | OS 11.1 |

### Liabilities
| Signal | Possible cause | Test | Detail |
|---|---|---|---|
| Long-term assets funded with short-term debt | Refinancing/liquidity risk | Maturity profile vs CFO | [liabilities-debt.md](./liabilities-debt.md); LY 12.2 |
| Accrued liabilities or warranty reserves falling vs activity | Under-accruing expenses | Provision roll-forwards | JN 2.5; OS 12.3 |
| "Reasonably possible" contingencies, low-end accruals | Hidden losses | Contingency note | OS 12.3 |
| Covenant near breach; waivers; debt reclassified | Distress | Debt note | OS 12.3 |
| Off-balance-sheet entities | Hidden leverage (Enron) | Notes on SPEs/VIEs, guarantees | OS 8.7 |
| Gains on debt extinguishment | Non-operating income | Exclude | JN 5.4.6 |
| Unremitted payroll/sales taxes | Cash distress | Current liabilities | JN 5.1–5.2 |

### Equity and per-share data
| Signal | Possible cause | Test | Detail |
|---|---|---|---|
| EPS growing faster than net income | Buybacks targeting EPS | Share count trend; pay tied to EPS | [equity-eps.md](./equity-eps.md); OS 14.5 |
| Buybacks funded with debt or above intrinsic value | Value destruction | Buyback price vs value; leverage trend | OS 14.2 |
| Dividends rising while income flat and liquidity worsening; dividends funded by borrowing | Unsustainable payout | Payout vs FCF; financing section | LY 12.5, 11.3 |
| Prior-period adjustments / restatements | Error or smoothing; investors view with "deep suspicion" | Retained-earnings bridge | OS 14.4 |
| Large negative OCI | Losses bypassing net income | Comprehensive income vs net income | OS 14.4; JN 4.10 |
| Shares issued for non-cash assets or services | Inflated valuations, hidden compensation | Equity note | OS 14.2; JN 6.4 |
| Reverse split | Delisting risk | Corporate actions | OS 14.3 |
| Cumulative preferred dividends in arrears | Senior claim ahead of common | Equity note | LY 10.3; JN 6.9 |

### Cash flow
| Signal | Possible cause | Test | Detail |
|---|---|---|---|
| CFO persistently below net income | Uncollectible revenue or understated expenses (OS 16.1) | Cumulative CFO/NI | [cash-flow-statement.md](./cash-flow-statement.md) |
| Negative FCF with rising net income | Lehman pattern | FCF trend | OS 16.5 |
| CFO boosted by stretched payables | Unsustainable | DPO trend | OS 16.2 |
| IFRS classification choices raising CFO | Comparability | Reclassify interest/dividends | OS 16.5 |
| Non-cash transactions misclassified | Distorted capex/FCF | Non-cash disclosures | OS 16.2 |

### Income statement presentation
| Signal | Possible cause | Test | Detail |
|---|---|---|---|
| Net income growth ≪ operating income growth (or the reverse) | Non-operating items driving results | Walk from operating income to net income | JN 7.3.1 |
| High net margin from investment gains | Low-quality earnings (Schneider) | Common-size comparison | JN 7.3.3 |
| Large non-operating income share (LY XYZ: rent > 2/3 of pretax income) | Earnings not from the core business | Multi-step statement | LY 5.5 |
| Discontinued operations used repeatedly | Burying recurring losses | Continuing-ops EPS trend | LY 11.4 |
| Single-step income statement | Less analytical detail ("keeps sensitive information out of the hands of competitive companies") | Look for segment and nature-of-expense notes | LY 11.4 |

### Governance and controls
| Signal | Source |
|---|---|
| No segregation of duties; management override | OS 8.2, 8.7 (HealthSouth, Currier) |
| Key staff never take vacation; sole system access | OS 8.1 (SCICAP) |
| Auditor also provides consulting; long-tenured lead partner (SOX: max 7 years, then 2 off) | OS 8.2 |
| Material weakness under SOX 404; qualified opinion; going-concern paragraph | OS 8.2; LY 4.4 |
| Audit committee not fully independent | LY 4.5 |
| Late filings; auditor resignation; CFO turnover | [analyst practice] |
| Delisting to avoid SOX ("has not proven to be a viable option"; read as a sign of trouble) | OS 8.2 |
| Related-party loans (e.g., non-interest shareholder loan) | LY 4.3 |

---

## 4. Screening Tools

- **Beneish M-Score** [OS 9.4]: eight ratios to flag manipulation; Cornell students used it to sell Enron a year before collapse. [Outside the books, the eight indices are: days sales in receivables, gross margin, asset quality, sales growth, depreciation, SG&A, leverage, and total accruals to total assets. Scores above roughly −1.78 are commonly treated as elevated risk. Compute from filings rather than relying on a third-party score.]
- **Accruals check** [derived from OS 16.1 and LY 11.3]: (Net income − CFO) ÷ average total assets. Persistently high positive accruals mean earnings outrun cash.
- **Gross-profit-method inventory test** [LY 6.4]: estimate ending inventory from historical margin; compare with reported.
- **Ratio trend vs peers** [OS 9.4]: "An investor or lender can compare ratio analysis to others in the industry, and year-to-year trend analysis can be helpful."

---

## 5. Forensic Workflow for the Skill

1. **Gatekeepers:** auditor, opinion type, going-concern, SOX 404 conclusion, auditor/CFO changes, restatements.
2. **Incentives:** pay metrics, covenants, upcoming financings or acquisitions, insider trading (Munger incentive check).
3. **Cash vs earnings:** 5–10 years of NI, CFO, capex, FCF; accrual ratio; CFO/NI.
4. **Working capital:** AR, inventory, AP, deferred revenue vs sales; DSO, DSI, DPO trends vs peers.
5. **Estimates:** bad-debt, warranty, depreciation lives/salvage, inventory write-downs, contingencies; any changes and their profit effect.
6. **Capitalization:** capex/depreciation, capitalized interest/development, other assets growth.
7. **Below-the-line items:** gains, discontinued operations, OCI, prior-period adjustments; normalize EPS.
8. **Off-balance-sheet and contingent claims:** SPEs, guarantees, reasonably possible losses, preferred arrears, unconsolidated investees.
9. **Per-share engineering:** buybacks vs net income growth, dilution, splits.
10. **Verdict input:** if two or more independent red flags appear in different areas (e.g., DSO rising + CFO/NI falling + estimate changes), downgrade confidence and widen the margin of safety; if fraud is plausible and unresolvable from public data, classify as **Too hard** (Munger basket) rather than forcing a valuation.
