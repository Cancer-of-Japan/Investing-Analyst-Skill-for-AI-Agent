# The Statement of Cash Flows and Free Cash Flow

Sources: [OS] OpenStax Ch 16 (and 5.3, 12.1); [LY] Lyryx Ch 11; [JN] Jonick Ch 7.2. Full citations in [accounting-foundations.md](./accounting-foundations.md).

Cash is the hardest number to fake. LY (verbatim): the cash flow statement "excludes non?‘cash accruals like depreciation and interest, making the statement of cash flows harder to manipulate than the other financial statements," and "revenue is vanity, profits are sanity, but cash is king" [LY 11.5 App B].

---

## 1. Why It Matters

- "It is quite possible for a profitable business to be short of cash??Conversely, an unprofitable business might have sufficient cash to pay its bills if it has access to enough financing" [LY 11.1].
- "even with a positive income position??a company can go bankrupt due to poor cash flow??even if a company has a lot of cash, it may still be in bankruptcy trouble if all or much of that cash is borrowed" [OS 5.3].
- **Earnings quality:** "A company that has records that show significantly less cash inflow on the statement of cash flows than the reported net income??could very well be reporting revenue for which cash will never be received from the customer or underreporting expenses" [OS 16.1].
- LY: "Users will be more confident in a company with a high correlation between cash provided by operations and net income measured under the accrual basis" [LY 11.3].
- Siegel in the *CPA Journal*, quoted by OS: "as Wall Street analysts have lost faith in earnings-based metrics in the wake of Enron, WorldCom, and others, many have gravitated toward the cash flow statement. Companies are regularly evaluated on the basis of free cash flow yield" [OS 16.5].
- It "is not a substitute for an income statement" [LY 11.3]; use both.

**Cash equivalents:** quickly convertible to a known amount of cash with insignificant risk; LY uses maturity ??3 months from acquisition [LY 11.1].

---

## 2. Classification

| Section | US GAAP content | Sources |
|---|---|---|
| **Operating** | Day-to-day: customers, suppliers, employees, **plus interest received and paid, dividends received, and income taxes** | OS 16.2; JN 7.2.1 |
| **Investing** | Buying/selling long-term assets: PP&E, land, patents, investments in stocks and bonds | OS 16.2; JN 7.2.1 |
| **Financing** | Issuing/repaying debt, issuing shares, buying treasury stock, **paying dividends** | OS 16.2; LY 11.2; JN 7.2.1 |
| **Non-cash investing & financing** | Asset bought with debt or shares, debt-for-equity swaps, stock dividends; **excluded from the statement but disclosed** | LY 11.2; OS 16.3 |

**IFRS choices** [OS Table 16.1]:

| Item | US GAAP | IFRS |
|---|---|---|
| Interest paid | Operating | Operating or financing |
| Interest received | Operating | Operating or investing |
| Dividends paid | Financing | Operating or financing |
| Dividends received | Operating | Operating or investing |
| Taxes | Operating | Usually operating; can be split |

**World-Wide Co.** [OS 16.5]: under US GAAP, CFO $2,500,000 ??capex $1,000,000 = FCF $1,500,000. Reclassifying under IFRS (interest paid to financing +$200,000, dividends received to investing ??50,000, investing-related taxes +$60,000) gives **FCF $1,710,000** with identical economics. "the flexibility afforded by IFRS can have an impact on comparability between companies." **Normalize classifications before comparing CFO or FCF.**

**Misclassification example** [OS 16.2 T-Shirt Pros]: a $200,000 warehouse bought with a note was wrongly shown as both a financing inflow and an investing outflow; "the calculation of free cash flow by outside analysts could be affected significantly."

---

## 3. Indirect Method (Operating Section)

"the vast majority of financial statements are presented using the indirect method" [OS 16.1]; JN: "The indirect method is more popular"; LY says it is more common in Canada.

**Steps** [OS 16.3; JN 7.2.3; LY 11.2]:
1. Start with **net income**.
2. **Add back non-cash expenses:** depreciation, amortization, depletion, amortization of bond discount [JN]. (Analyst addition: stock-based compensation and impairments are also added back in practice.)
3. **Reverse non-operating gains and losses:** subtract gains, add losses (the cash proceeds go to investing/financing).
4. **Working capital:**

| Change | Adjustment |
|---|---|
| Increase in current asset (AR, inventory, prepaid) | **Subtract** |
| Decrease in current asset | Add |
| Increase in current liability (AP, wages, taxes payable, unearned revenue) | **Add** |
| Decrease in current liability | Subtract |

(Dividends payable is excluded because dividends are financing [LY 11.2].)

### Worked examples

**OS Propensity Company 2018** [OS 16.3]:

| Line | Amount |
|---|---|
| Net income | 4,340 |
| + Depreciation | 14,400 |
| ??Gain on sale of land | (4,800) |
| ??Increase prepaid insurance | (700) |
| ??Increase inventory | (2,500) |
| + Decrease AR | 4,500 |
| + Increase salaries payable | 400 |
| ??Decrease AP | (1,800) |
| **Cash from operations** | **13,840** |
| Investing: land sold +14,800; plant ??0,000 | (25,200) |
| Financing: stock +45,000; note repaid ??0,000; dividends ??40 | 34,560 |
| Non-cash: land acquired for a $20,000 note | disclosed |

**JN Jonick Company** [JN 7.2]: net income $48,000 + depreciation 5,000 ??gain on investments 10,000 + loss 1,000 + AR decrease 24,000 ??inventory increase 32,000 + prepaid decrease 6,000 + AP increase 7,000 ??wages payable decrease 3,000 = **CFO $46,000**; investing +$28,000 (land and investment sales $189,000, equipment purchases $161,000); financing ??36,000 (stock +20,000, bonds redeemed ??0,000, dividends ??,000); cash +$38,000.
- [Analyst note] CFO ??net income, but the $10,000 gain inflated net income without operating cash, and a $32,000 inventory build was funded largely by collecting receivables.

**LY Example Corporation 2023 ($000s)** [LY 11.2??1.3]: net income 80; CFO 70 (inventory +450 offset by depreciation 260, AR ??5, AP +90); investing ??,040 (building and machinery 1,070); financing +847 (loan 500, shares 410, dividends ??3); cash fell 123.

**Useful financing formula** [JN 7.2.3]: Cash dividends paid = Beginning dividends payable + Dividends declared ??Ending dividends payable (8,000 + 3,000 ??5,000 = 6,000).

**Investing rule** [JN 7.2.3]: cash from an asset sale = book value removed + gain (or ??loss). An asset account can have both a sale and a purchase in one year; reconstruct the ledger rather than netting.

---

## 4. Direct Method (Operating Section)

Lists actual receipts and payments. Both IFRS and US GAAP "recommend and encourage the direct method" [OS 16.6]; LY: "IFRS standards prefer its use." Companies avoid it because collecting cash-only data is costly and it reveals sensitive figures [LY 11.5]. US GAAP requires the indirect reconciliation as well if direct is used [OS 16.6].

**Conversion formulas** [JN 7.2.4; OS 16.6]:
- Cash from customers = Beginning AR + Sales ??Ending AR (JN: 58,000 + 174,000 ??34,000 = **$198,000**).
- Purchases = Ending inventory + COGS ??Beginning inventory (JN: 112,000 + 94,000 ??80,000 = 126,000).
- Cash paid to suppliers = Beginning AP + Purchases ??Ending AP (JN: 22,000 + 126,000 ??29,000 = **$119,000**).
- Cash paid for wages = Beginning wages payable + Wages expense ??Ending wages payable (JN: 17,000 + 20,000 ??14,000 = $23,000).
- Cash paid for insurance = Ending prepaid + Insurance expense ??Beginning prepaid.
- (Add unearned-revenue changes to cash from customers: LY Watson's cash from sales fell as unearned revenue dropped $200,000.)

**Same answer either way:** JN shows $46,000 under both methods [JN 7.2.5].

**LY Watson Ltd.:** net income $77,000 but **operating cash flow ??101,660** [LY 11.5]. A profitable income statement can sit on top of cash burn.

**Investor use:** even when a company reports indirect, you can rebuild direct-method cash from customers using the formula above; compare it with reported revenue. A widening gap is a revenue-quality warning.

---

## 5. Free Cash Flow and Cash Flow Ratios

**OS definitions** [OS 16.5]:

$$\text{Free cash flow}=\text{Cash from operations}-\text{Capital expenditures}-\text{Cash dividends}$$

$$\text{Cash flows to sales}=\frac{\text{FCF}}{\text{Sales}}\qquad\text{Cash flows to assets}=\frac{\text{FCF}}{\text{Total assets}}$$

- OS uses *expected or planned* capex and dividends; elsewhere (16.2, World-Wide box) it defines FCF as CFO ??capex only. **State which definition you use.** The common analyst definition, and the one consistent with Buffett's owner earnings, is **CFO ??capex** (before dividends, because dividends are a use of free cash, not a cost of the business). For owner earnings, subtract only **maintenance** capex and deduct stock-based compensation if it was added back.
- These measures "give indicators about the company's flexibility and agility??ability to seize opportunities in the future" [OS 16.5].
- Propensity FCF: 13,840 ??40,000 ??440 = **??26,600** [derived]; the ratios are "not useful" when FCF is negative.
- "The absence of free cash flow is an indicator of severe liquidity concern??could be an early indicator that the company may not be able to continue operations" ??but a one-time large capex funded from reserves "would not be an issue of concern" [OS 16.5].
- OS mentions operating cash flow ratio, cash flow margin, and **free cash flow yield** without formulas. Standard forms [analyst practice]: CFO Ã· current liabilities; CFO Ã· sales; FCF per share Ã· price.

**Lehman Brothers** [OS 16.5]: net income rose from $3.1B (2005) to $4.1B (2007) and it held $7.2B of cash at end-2007, yet it failed in September 2008, "the biggest corporate bankruptcy in history." "The large negative free cash flow gave warning that Lehman Brothers was a risky investment."

---

## 6. Reading Patterns

The books interpret individual cases rather than giving a sign-pattern table. These patterns combine their examples:

| Pattern (CFO / CFI / CFF) | Typical meaning | Book case |
|---|---|---|
| + / ??/ ??| Mature, self-funding: operations pay for capex, debt repayment and dividends | ??(healthy benchmark) |
| + (below NI) / ?’â? / ++ | Expansion funded externally; CFO lagging NI due to inventory/receivables build | LY Example Corp: CFO 70 vs NI 80, capex 1,070 "primarily" funded by financing; "may indicate looming cash flow problems, particularly if the trend continues" |
| ??/ Â± / + (incl. dividends paid) | Profitable on paper, burning cash, borrowing to pay dividends | LY Wellbourn: NI $80,500, CFO ??26,200, $160,000 bonds issued partly to pay $50,000 dividends |
| ??/ ??/ + | Start-up or distressed; dependent on capital markets | OS: substantially negative CFO "could be a warning sign of possible impending doom" |
| + / + / ??| Selling assets to repay debt or fund payouts; shrinking | Check whether asset sales are recurring |
| CFO boosted by payables | Stretching suppliers; not sustainable | OS 16.2 Amazon: CFO helped by AP +$78B vs inventory +$20B (book figures inflated ~1,000?) |
| Large negative CFI with loss | Heavy investment; judge by returns on that capex | OS 16.1 Amazon hypothetical |

LY on cash levels: "Excess cash on hand is unproductive. Conversely, inadequate cash decreases liquidity" [LY 11.3].

---

## 7. Manipulation and Distortion Points

- **Capitalizing operating costs** (WorldCom) moves outflows from operating to investing, inflating CFO; FCF is unaffected only if you subtract all capex [OS 11.2].
- **Stretching payables** lifts CFO temporarily [OS 16.2].
- **Selling receivables** (factoring) or cutting inventory at period-end lifts CFO once.
- **IFRS classification choices** can move interest and dividends out of operating [OS 16.5].
- **Misclassified non-cash transactions** distort capex and FCF [OS 16.2].
- **Gains on sale** are in net income but their cash is in investing; reversing them in CFO is correct ??don't count the proceeds as recurring.
- **Acquisitions** are investing outflows; serial acquirers can show strong CFO and "FCF before acquisitions" while spending most cash on purchases. Treat recurring acquisitions as capex.

---

## 8. Investor Checklist: Cash Flow

1. CFO vs net income for 5??0 years; cumulative ratio well below 1 is a red flag.
2. Decompose CFO: depreciation add-back vs working-capital changes; identify AR, inventory and AP drivers.
3. FCF = CFO ??capex (state definition); FCF per share and FCF yield; FCF after acquisitions for serial acquirers.
4. Maintenance vs growth capex for owner earnings (see [buffett.md](../Investors/buffett.md)).
5. Who funds what: are capex, dividends and buybacks covered by CFO, or by new debt/equity?
6. Non-cash investing/financing disclosures (assets acquired with debt are capex too).
7. Normalize IFRS vs US GAAP classifications before peer comparison.
8. Rebuild cash from customers and compare with revenue.
