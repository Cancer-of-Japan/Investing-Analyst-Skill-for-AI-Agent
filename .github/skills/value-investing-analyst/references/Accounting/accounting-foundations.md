# Accounting Foundations for Investors: Framework, Accruals, Statement Links, Notes, Audit

Sources (cited by tag and section throughout the Accounting references):
- **[OS]** Franklin, Graybeal, Cooper, *Principles of Accounting, Vol. 1: Financial Accounting* (OpenStax, 2019), US GAAP with IFRS boxes. [Book](../../../../../Books/Accounting%20Books/%5BAccounting%2001%5D%20Mitchell%20Franklin_%20Patty%20Graybeal_%20Dixon%20Cooper_%20OpenStax%20-%20Principles%20of%20Accounting%2C%20Volume%201_%20Financial%20Accounting%201%20%282019%2C%20OpenStax%29%20-%20libgen.li.md)
- **[LY]** Dauderis & Annand, adapted by Jensen & Morpurgo, *Introduction to Financial Accounting* (Lyryx, 2024-A-D), IFRS / Canadian. [Book](../../../../../Books/Accounting%20Books/OTB_011_13_Introduction_to_Financial_Accounting_2024_A_D_037d1c071f.md)
- **[JN]** Christine Jonick, *Principles of Financial Accounting* (University of North Georgia Press, 2018), US GAAP. [Book](../../../../../Books/Accounting%20Books/Principles%20of%20Financial%20Accounting%7BChristine%20Jonick%7D%282018%2C%20University%20of%20North%20Georgia%29%7B94003594%7D%20libgen.li.md)

Use this file to understand *how* the numbers in a filing are produced, so you know which numbers are hard facts, which are estimates, and where management has discretion. The companion files go deeper by topic:

| Topic | File |
|---|---|
| Revenue, receivables, bad debts, earnings management | [revenue-receivables.md](./revenue-receivables.md) |
| Inventory, COGS, gross margin | [inventory-cogs.md](./inventory-cogs.md) |
| PP&E, depreciation, intangibles, goodwill, investments in securities | [long-lived-assets-investments.md](./long-lived-assets-investments.md) |
| Current liabilities, contingencies, notes, bonds | [liabilities-debt.md](./liabilities-debt.md) |
| Share capital, buybacks, dividends, EPS, book value | [equity-eps.md](./equity-eps.md) |
| Statement of cash flows, free cash flow | [cash-flow-statement.md](./cash-flow-statement.md) |
| Ratios, horizontal/vertical analysis, DuPont | [ratio-analysis.md](./ratio-analysis.md) |
| Fraud, internal control, manipulation checklist | [red-flags-forensics.md](./red-flags-forensics.md) |

**Scope warning.** These are introductory textbooks (2018–2024). They teach the logic well but omit or predate several current standards: the full ASC 606 / IFRS 15 five-step revenue model, lease capitalization (ASC 842 / IFRS 16), expected-credit-loss models (CECL / IFRS 9), diluted EPS calculation, segment reporting, and deferred taxes in depth. When a company's numbers depend on those, read the filing's own notes and say the textbook rule is simplified.

---

## 1. Who Sets the Rules and Why It Matters

- **US GAAP** is set by the **FASB**; the **SEC** enforces it for public companies and "delegates the process of setting standards for US GAAP to the FASB" [OS 3.1].
- **IFRS** is set by the **IASB** and used in "120 or more different countries" [OS 3.1]. In Canada, publicly accountable enterprises (PAEs) use IFRS; private enterprises (PEs) may use IFRS or the "less onerous" ASPE [LY 1.3].
- GAAP has detailed, industry-specific guidance; IFRS is more principles-based. "Different standards produce different results" [OS 5.3]. Same economics can show different numbers.
- Audits of US public companies are done by auditors overseen by the **PCAOB**; the external auditor reports to the **audit committee**, not management [OS 3.1].

**Investor rule:** Before comparing two companies, check the framework (US GAAP vs IFRS vs local GAAP), the fiscal year-end, and the currency. Key GAAP/IFRS differences that move ratios are listed in Section 8.

---

## 2. Qualitative Characteristics: What "Useful" Information Means [LY 1.3]

| Characteristic | Book definition | What to test as an investor |
|---|---|---|
| **Relevance** (primary) | "has the ability to make a difference in the decision‑making process" | Does the disclosure actually explain the drivers of value? |
| **Faithful representation** (primary) | "is complete, neutral, and free from error" | Are estimates neutral or consistently optimistic? |
| Comparability | businesses use similar accounting practices | Same methods as peers and as prior years? |
| Verifiability | others can confirm the information | Can you tie numbers across statements and notes? |
| Timeliness | available in time to be useful | Late filings are a warning sign |
| Understandability | clear and concise | Obscure language around key items is a warning sign |

LY: "To be useful, information must be relevant and faithfully represent a business's economic activities. This requires ethics."

---

## 3. The Principles and Assumptions (combined from LY Table 1.1 and OS 3.1)

| Principle / assumption | Rule | Book example | Investor implication |
|---|---|---|---|
| **Business (separate) entity** | Separate records per entity | Owner's personal car not on the books [OS] | Watch related-party transactions that blur the entity line |
| **Going concern** | Assume the business continues for the foreseeable future (often 12 months) | Business Z certain to lose a $20M lawsuit must disclose a going-concern issue [LY] | OS red flags: "defaults on loans or a sequence of losses." A going-concern paragraph in the audit report is a major warning |
| **Monetary unit** | Stable currency; inflation ignored | Land bought 1940 for $5,000 stays at $5,000 [LY] | Old assets understate replacement cost; real returns on old asset bases are overstated |
| **Time period** | Results split into years/quarters | — | Cut-off choices around period-end move profit |
| **Historical cost** | Record at actual cost; don't mark up for market changes | Truck advertised $75,000, paid $70,000 → $70,000 [LY]; equipment bought $40,000 thought worth $60,000 stays $40,000 [OS] | Book value can understate land/brands and overstate obsolete assets; hidden asset value is a Graham/Icahn opportunity |
| **Revenue recognition** | Record when earned, not when cash moves | Sale Mar 5, cash Apr 5 → revenue Mar 5 [LY] | Revenue is an estimate-laden number; see [revenue-receivables.md](./revenue-receivables.md) |
| **Matching / expense recognition** | Expenses in the period of the related revenue, or the period they occur | Supplies bought Mar 15 are an asset, expensed as used [LY] | "A mismatch… could be an understated net income in one period with an overstated net income in another" [OS] |
| **Full disclosure** | Report anything users need, usually in notes | Firm seeking a $1M loan must disclose a certain $20M lawsuit loss [LY] | Notes are mandatory reading, not optional |
| **Consistency** | Same policies period to period; changes disclosed | Inventory method cannot flip next year [LY] | A policy change that lifts profit is a red flag |
| **Materiality** | Proper treatment only for items that affect decisions | $5 stapler expensed [LY]; office equipment ≤$100 expensed [LY 4.1] | Many small "immaterial" choices can add up |
| **Conservatism** | Under uncertainty, record expected losses but not expected gains [OS 3.1]; "the approach that shows the results in the least favorable light should be presented" [JN 4.1.3] | LCM write-downs; contingent gains never booked | Asymmetry: losses hit early, gains wait until realized |

**Recognition criteria** [LY 3.1]: an item is recognized when (1) "it is probable that any future economic benefit associated with the item will flow to the business; and (2) it has a value that can be measured with reliability."

---

## 4. The Accounting Equation and How the Statements Link

$$\text{Assets} = \text{Liabilities} + \text{Equity}$$

- Equity = share capital (paid in by owners) + retained earnings (cumulative net income − dividends) [LY 1.4; JN 1.7].
- JN's truck example: buy a $30,000 truck with $10,000 down and a $20,000 loan → 30,000 = 20,000 + 10,000. Every asset is paid for with "your own money" (equity) or "other people's money" (liabilities) [JN 1.7].

**Order and links** [LY 1.4, 2.3; JN 1.7.4]:

```
Income statement  ──net income──►  Statement of changes in equity / retained earnings
                                         │ ending share capital & retained earnings
                                         ▼
                                    Balance sheet  ◄── cash balance ── Statement of cash flows
```

- Income statement: revenues − expenses = net income for a **period**.
- Statement of changes in equity: opening equity + shares issued + net income − dividends = closing equity.
  - JN example: 12,000 + 6,000 + 3,000 − 1,000 = 20,000 [JN 1.8]. Rearranged, you can solve for any missing number, e.g. implied net income.
- Balance sheet: position at a **point in time**. Dividends never appear on it [JN 1.7.4].
- Cash flow statement: reconciles opening to closing cash.

**Investor check (tie-out):** closing retained earnings − opening retained earnings should equal net income − dividends declared ± explicit adjustments. Any unexplained difference points to items bypassing the income statement (OCI, prior-period restatements, buyback charges). See [equity-eps.md](./equity-eps.md).

**Profitable but cash-poor, illustrated:** In Big Dog Carworks' first month, net income was +$2,200 but operating cash flow was −$1,100, because receivables (+$2,000) and prepaid insurance (+$2,400) absorbed cash [LY 1.4].

---

## 5. Accrual Accounting and the Four Adjusting Entries

**Accrual basis:** "recognizes economic events when they take place, regardless of when the related cash transactions occur" [JN 2.1]. LY: accrual "forms the basis of GAAP" [LY 3.1].

**Why cash-basis profit can be faked:** "If your company was having a bad year and you do not want to report a loss, just do not pay the bills for the last month of the year and you can suddenly show a profit in a cash-basis system" [OS 5.3]. Accrual accounting fixes timing but introduces estimates instead.

**Operating cycle** [LY 3.1]: cash → buy inputs/pay expenses → earn revenue → collect cash. Length runs from about a week (grocery) to a year (car dealer). Statements cut the cycle mid-stream, so open items must be adjusted.

**Matching timeline** [JN 2.2]: three $100 jobs and three $60 costs straddling May–July. June revenue = $50 + $100 + $50 = $200; June expenses = $30 + $60 + $30 = $120; June net income $80. Adjustments "chop off" the parts belonging to other periods.

### The four adjustment types and what goes wrong if omitted [JN 2.3–2.5; LY 3.2 adds depreciation as a fifth]

| Type | Entry | Example | If omitted: income | Assets | Liabilities | Equity |
|---|---|---|---|---|---|---|
| **Deferred expense** (prepaid, supplies, depreciation) | Dr Expense / Cr Asset (or Accum. Depreciation) | $1,000 supplies, $100 used [JN] | **Overstated** | Overstated | — | Overstated |
| **Deferred revenue** (unearned) | Dr Unearned revenue / Cr Revenue | $1,000 prepaid, $600 earned [JN] | Understated | — | Overstated | Understated |
| **Accrued expense** (wages, interest, taxes) | Dr Expense / Cr Payable | 2 days of wages $400 at month-end [JN] | **Overstated** | — | Understated | Overstated |
| **Accrued revenue** | Dr Receivable / Cr Revenue | $2,500 of a two-month job earned in June [JN] | Understated | Understated | — | Understated |

**Investor reading** [JN analyst-oriented summary]:
- Omitting or under-accruing **expense-side** adjustments flatters profit. Look for falling accrued liabilities while activity grows.
- Booking **revenue-side** accruals aggressively (accrued revenue, early release of unearned revenue) also flatters profit. Look for unbilled receivables or contract assets growing faster than sales.
- Every adjustment touches one income-statement account and one balance-sheet account [JN 2.2.1]. So profit manipulation always leaves a balance-sheet footprint, usually in receivables, inventory, prepaid/capitalized costs, or accrued liabilities. Track those balances against sales.

**Mixed accounts** [LY 3.2]: an account with both a balance-sheet and an income-statement portion (e.g., prepaid insurance partly used). The split is a judgment.

**Closing entries** [LY 3.6; JN 1.4.4]: revenue, expense and dividend accounts are zeroed into retained earnings each period. Skipping closing would merge periods (JN's stopwatch analogy: 50s + 45s reported as 95s). Not an investor issue in audited statements, but it explains why retained earnings is the cumulative bridge.

---

## 6. The Classified Balance Sheet [LY 4.2; JN 4.8.1]

- **Current assets:** cash or items expected to be converted to cash or consumed "during the next year or within the operating cycle of the entity, whichever is longer" [LY 4.2]. Listed by decreasing liquidity: cash, short-term investments, receivables, inventory, prepaids.
- **Non-current assets:** long-term investments; PP&E (at cost less accumulated depreciation); intangibles; goodwill (separate line).
- **Current liabilities:** due within 12 months or the operating cycle, whichever longer; includes the **current portion of long-term debt** and unearned revenue [LY 4.2; OS 12.1].
- **Non-current liabilities:** mortgages, bonds, long-term notes.
- **Comparatives:** "Financial statement information must be disclosed for the most recent year with the prior year for comparison" [LY 4.2].

**Big Dog example, why classification changes ratios** [LY 4.2]:

| | 2023 | 2022 |
|---|---|---|
| Total current assets | 158,000 | 136,570 |
| Total current liabilities | 78,000 | 114,250 |
| Long-term borrowings | 163,145 | 0 |
| Total equity | 43,500 | 32,750 |

The current ratio rose from 1.20 to 2.03 only because a mortgage moved debt from current to long-term, while total debt to equity rose from 3.49 to 5.54 [derived]. **A better current ratio can coexist with much higher leverage.**

**Historical cost and inflation** [LY 4.1]: land bought for $100,000 that rises to $125,000 stays at $100,000; $50,000 cash loses purchasing power under 10% inflation with no recorded loss. Balance sheets of old companies can hide both appreciated real estate and eroded real value.

---

## 7. Notes, the Auditor's Report, and Management's Responsibility

### Notes to the financial statements
"In accordance with the disclosure principle, notes to the financial statements provide relevant details that are not included in the body of the financial statements" [LY 4.3]. LY's sample notes show what to read, in this order:

1. **Nature of operations** and basis of preparation (framework, listing, approval date).
2. **Accounting policies:** revenue measurement; when expenses are recognized; **borrowing costs capitalized** during construction (lifts current profit); PP&E measurement, depreciation method and useful lives (buildings 25y, equipment 10y, truck 5y in the example); income-tax basis.
3. **Estimation uncertainty:** "Actual results may be substantially different."
4. **PP&E roll-forward:** gross cost, additions, disposals, depreciation, impairments, by class.
5. **Borrowings:** rate, security, maturity, covenants, related-party loans. Big Dog's note reveals a 6% demand loan secured by receivables and inventory, a non-interest-bearing **shareholder loan**, and a 5% mortgage whose terms are **renegotiated in 2026** (refinancing risk) [LY 4.3].
6. **Share capital:** classes, votes, shares issued.
7. Also expected per OS/LY: inventory method, bad-debt estimation method, contingencies, dividends in arrears, non-cash investing/financing, and any change in accounting policy.

LY 12.1: notes are "an integral part" of analysis and a key source of qualitative information.

### Auditor's report [LY 4.4]
- An audit is "an external examination of a company's financial statement information and its system of internal controls."
- "An audit seeks not certainty, but reasonable assurance that the financial statement information is not materially misstated."
- Components: addressee and independence, statements audited, management's responsibility, auditor's responsibility (internal control considered "not for the purpose of expressing an opinion on the effectiveness of the entity's internal control" in LY's Canadian private-style sample), evidence sufficiency, **opinion** ("present fairly, in all material aspects…"), signature and date.
- LY simplifies opinions to two: "an unqualified auditor's report indicates that the financial statements are truthful and a qualified auditor's report is one that indicates the financial statements are not or may not be truthful." [Outside these books: modern reports also include adverse opinions, disclaimers, going-concern paragraphs, and critical/key audit matters. Treat anything other than a clean opinion, or any going-concern paragraph, as a serious red flag.]
- **SOX for US public companies** [OS 8.2]: the auditor issues an internal-control report; non-audit services to audit clients are limited; lead audit partner rotates after at most 7 years with a 2-year break; under **Section 404** management must annually assess and attest to internal control over financial reporting. A reported **material weakness** deserves heavy weight.

### Management's responsibility [LY 4.5]
- Management prepares the statements, "including the estimates" (useful lives, bad debts, warranties). The auditor checks "the reasonableness of estimates."
- The **audit committee** should consist solely of directors who are not employees; it meets the auditor, who has unrestricted access.
- **Investor implication:** every estimate is management's number. The auditor tests reasonableness, not optimality. Where management incentives are tied to EPS (see [equity-eps.md](./equity-eps.md)), assume estimates lean favourable unless evidence says otherwise.

---

## 8. US GAAP vs IFRS Differences That Change Analysis

| Area | US GAAP | IFRS | Source |
|---|---|---|---|
| LIFO inventory | Allowed (about 35–40% of US companies use it; LIFO conformity rule ties tax and books) | **Banned** | OS 10.1 |
| Effect on current ratio | LIFO in rising prices → lower inventory, lower current ratio | FIFO → higher | OS 5.3 |
| Impairment reversal | Not discussed as allowed | Reversals allowed if recoverable amount recovers | LY 8.5 |
| PP&E revaluation | Cost only | May revalue a class to fair value | LY 8.5; OS 11.3 |
| Component depreciation | Usually whole asset | Major components depreciated separately | LY 8.4; OS 11.3 |
| Probable threshold for provisions | Often ~80% likelihood | "More likely than not," ~50% | OS 12.3 |
| Measuring a loss range | Accrue the **low end** | Accrue the **discounted midpoint** | OS 12.3 |
| Debt in covenant breach | Stays non-current if refinanced before statements are issued | Arrangements needed **by year-end** | OS 12.3 |
| Completed-contract revenue | Allowed when estimates unreliable | Not allowed; revenue = costs until estimable | OS 9.5 |
| Interest/dividends in cash flow | Interest paid & received, dividends received → operating; dividends paid → financing | Choice: interest paid operating or financing; dividends paid operating or financing; interest/dividends received operating or investing | OS 16.2 |
| Effective-interest bond amortization | Required unless straight-line is immaterial | Required, no exceptions | OS 13.2 |
| Bond premium/discount accounts | Separate accounts | Net carrying value | OS 13.3 |
| Balance sheet order | Most liquid first | May show reverse liquidity | OS 9.5 |

OS 16.5 World-Wide Co.: reclassifying interest paid, dividends received and some taxes under IFRS lifted free cash flow from $1,500,000 to $1,710,000 with no change in economics. **Normalize classifications before comparing FCF across frameworks.**

---

## 9. Investor Checklist: Before Using Any Reported Number

1. Framework, auditor, opinion type, any going-concern or material-weakness language.
2. Accounting policies note: revenue, inventory method, depreciation lives, capitalization policy (incl. borrowing costs), bad-debt method, warranty method.
3. Changes in policy or estimate this year and their effect on profit (estimate changes are prospective and often buried).
4. Roll-forwards: PP&E, intangibles/goodwill, allowance for doubtful accounts, warranty provision, debt maturities.
5. Tie-outs: retained earnings bridge; cash in balance sheet = cash-flow ending cash; segment totals = consolidated totals.
6. Balance-sheet footprints of accruals: receivables, inventory, capitalized costs and accrued liabilities vs sales growth.
7. Related-party balances (shareholder loans, management fees).
8. Classification choices that move ratios: current vs non-current debt, operating vs financing cash flows.
