# Equity, Buybacks, Dividends, Book Value, and Earnings per Share

Sources: [OS] OpenStax Ch 14; [LY] Lyryx Ch 10, 11.4, 12.5; [JN] Jonick Ch 6, 7.3.4. Full citations in [accounting-foundations.md](./accounting-foundations.md).

Per-share numbers drive Graham's number, Lynch's PEG, and Buffett's buyback test. They depend on share counts, preferred claims, and items that bypass the income statement.

---

## 1. Structure of Equity

- **Equity = Contributed (paid-in) capital + Retained earnings** (+ accumulated other comprehensive income ??treasury stock) [OS 14.4; LY 10.1; JN 6.7].
- **Retained earnings** = cumulative net income ??cumulative losses ??dividends declared; a negative balance is a **deficit** [OS 14.4].
- LY: "A corporation only receives money when shares are first issued." Secondary trading does not change the company's balance sheet [LY 10.1].
- **Share counts:** authorized ??issued ??outstanding. Outstanding = issued ??treasury shares [OS 14.1; JN 6.2]. OS Waystar: 2,000 authorized, 1,500 issued, 100 repurchased ??1,400 outstanding.
- **Par value** "has no economic significance" [OS 14.1]; amounts above par go to additional paid-in capital (APIC). Market value "does not appear in the corporation's accounting records."
- **Control:** more than 50% of voting shares controls the board; proxies concentrate votes [LY 10.1]. Dual-class structures appear as Class A/B shares [LY 10.1] (Icahn governance flag, see [icahn.md](../Investors/icahn.md)).
- **Preemptive right** [OS 14.1]: 50 of 1,000 shares = 5%; skipping a 200-share issue dilutes to 50/1,200 = 4.17%.

**JN equity section example** [JN 6.7]: preferred $1,000,000 + excess 10,000 + common 500,000 + excess 150,000 + treasury paid-in 2,000 = paid-in $1,662,000; + retained earnings 130,000; ??treasury stock 27,000 ??**total equity $1,765,000**. "Cash Dividends and Stock Dividends are not reported on the balance sheet."

---

## 2. Preferred Shares

- Dividends paid before common; usually non-voting; fixed dividend; ranked before common in liquidation; listed before common in equity [LY 10.1; JN 6.2].
- OS: "some researchers believe preferred stock has characteristics closer to that of a stock/bond hybrid security" [OS 14.1]. LY: preferred lets a company raise capital "without requiring existing shareholders to give up control."
- **Cumulative:** unpaid dividends accumulate as **dividends in arrears**, which must be paid before any common dividend. Arrears are **not a liability until declared, but must be disclosed in a note** [LY 10.3]. **Non-cumulative:** skipped dividends are lost forever [LY 10.3; JN 6.9].
- LY: preferred dividends are "often paid even if the corporation experiences a net loss" [LY 10.3].

**JN allocation example** (25,000 preferred at $3 = $75,000/yr; 100,000 common) [JN 6.9]:

| Year | Declared | Non-cumulative: to common | Cumulative: to common | Cumulative arrears at year-end |
|---|---|---|---|---|
| 1 | 0 | 0 | 0 | 75,000 |
| 2 | 20,000 | 0 | 0 | 130,000 |
| 3 | 60,000 | 0 | 0 | 145,000 |
| 4 | 175,000 | 100,000 | 0 | 45,000 |
| 5 | 200,000 | 125,000 | 80,000 | 0 |

**Investor reading:** arrears are a senior claim that sits ahead of common holders but outside the balance sheet. Deduct them (and the preferred's liquidation value) before computing common book value or per-share intrinsic value. Graham's NCAV subtracts preferred too (see [graham.md](../Investors/graham.md)).

---

## 3. Issuing Shares, Including for Non-Cash Assets

- Cash issue: La Cantina 8,000 shares ? $21.50 = $172,000 ??common (par $1.50) $12,000 + APIC $160,000 [OS 14.2].
- **Non-cash issues** are recorded at "the fair market value of the stock or the asset or services received, whichever is more clearly determinable" [OS 14.2].
  - LY: 2,500 preferred shares for land $35,000 + building $50,000 = $85,000 [LY 10.2].
  - JN: stock issued for land and for attorney/engineer services (organization costs) [JN 6.4].
- **Red flag:** shares issued for assets or services rely on a valuation management chooses; inflated values inflate assets and equity. Check related-party deals.
- Shares issued for services are a real cost (like stock-based compensation) even when no cash moves.

---

## 4. Treasury Stock and Share Retirement (Buybacks)

**Accounting rules**
- Treasury stock is a **contra-equity account, not an asset**: "An entity cannot own part of itself" [OS 14.2; JN 6.4]. It reduces total equity and shares outstanding; treasury shares get no dividends or votes.
- Reissue above cost credits APIC?�treasury; below cost debits APIC?�treasury and then **retained earnings**. It is **never a gain or loss**: "gains and losses only result from the disposition of economic resources (assets). Treasury Stock is not an asset" [OS 14.2; JN 6.4].
  - JN: buy 1,000 at $45; resell 200 at $60 ??+$3,000 paid-in capital; resell 200 at $40 ????1,000 paid-in capital.
- **Retirement** [LY 10.2]: buying back below average issue price credits contributed surplus; buying back above it reduces contributed surplus then **retained earnings** (LY: 150 shares at $11 vs $10 average ??$50 charged to retained earnings).
- "Many states restrict retained earnings by the cost of treasury stock" [OS 14.4].

**Why companies buy back** [OS 14.2]: block takeovers, "create demand for the stock, which in turn raises the market price," fund employee options. Examples: Disney bought back 74M shares in 2016; Nestlé's treasury stock rose from CHF 990M to CHF 4,537M in 2017.

**Effect on EPS** [OS 14.5 Ranadune]: net income $15,000 and 20,000 shares ??EPS $0.75; after buying back 2,500 shares, EPS $0.86 with no change in earnings.
- OS (verbatim): "managers understand how the number of shares outstanding can affect EPS and are often in position to manipulate EPS by creating transactions that target a desired EPS number."
- OS ethics box: S&P 500 buybacks ??$780B in 2017 (+30%); buybacks legalized in 1982; quoting Forbes, buybacks "can inflate a company's share price and boost its earnings per share?�metrics that often guide lucrative executive bonuses."

**Investor tests (combine with Buffett and Graham 1932, see [buffett.md](../Investors/buffett.md) and [graham-1932-return-cash.md](../Publication/graham-1932-return-cash.md)):**
1. Compare EPS growth with net income growth; the gap is buyback-driven.
2. Compare buyback price with a conservative intrinsic value; buybacks above value destroy value even when EPS rises.
3. Net buybacks = repurchases ??shares issued for options/compensation. Gross buybacks that only offset dilution do not shrink the share count.
4. Check whether buybacks are funded by debt (raises leverage) or by free cash flow.
5. Check whether executive pay is tied to EPS.

---

## 5. Dividends

**Prerequisites:** board declaration, sufficient cash, and sufficient retained earnings [JN 6.5; OS 14.3]. Paid-in capital is not available for dividends, which protects creditors (LY: assets $40,000, liabilities $39,000, common $900, retained earnings $100 ??maximum dividend $100) [LY 10.3].

**Dates** [OS 14.3; LY 10.3; JN 6.5]:
- **Declaration:** becomes a legal liability.
- **Record:** determines who receives it; shares bought after trade "ex dividend."
- **Payment** (or **distribution** for stock dividends).

Dividends are paid only on outstanding shares (JN: 30,000 issued ??10,000 treasury + 1,000 resold = 21,000 outstanding).

**Dividends are not expenses** and never appear on the income statement [OS 14.3].

**Why boards may not pay** [LY 10.3]: cash tied up in PP&E, growth reinvestment policy, no legal requirement, preference for share dividends.

**Dividend smoothing:** "paying dividends that are relatively equal period after period, even when earnings fluctuate" [OS 14.3]. Costco paid a regular $0.57 quarterly plus a $7.00 special dividend in 2017.

**Property dividends:** recorded at fair value (Disney park tickets; AB InBev beer) [OS 14.3].

**Red flag stated in the books:** Big Dog's dividends rose from $60 to $80 (2022??4) while net income was flat and liquidity was deteriorating. "Investors might ask why such high levels of dividends are being paid given this situation" [LY 12.5]. Derived payout: 53.6% ??59.8% ??69.0%. LY's Wellbourn example issued $160,000 of bonds partly to pay $50,000 of dividends while operating cash flow was negative [LY 11.3]. **Dividends funded by borrowing are a return of capital disguised as income.**

---

## 6. Stock Dividends, Splits, and Reverse Splits

"There is no change in total assets, total liabilities, or total stockholders' equity when a small stock dividend, a large stock dividend, or a stock split occurs" [OS 14.3].

| Event | Accounting | OS Duratech example (60,000 sh, $0.50 par, $9 market) |
|---|---|---|
| Small stock dividend (< 25%) | Retained earnings ??paid-in capital at **market value** | 5% = 3,000 sh; RE ??27,000 |
| Large stock dividend (> 25%) | At **par** | 30% = 18,000 sh; RE ??9,000 |
| Stock split | Memo entry only; par per share falls | 4-for-1 ??240,000 sh, price ??24 ??$6 |

- LY: 10% stock dividend leaves each holder's percentage unchanged (20/10/40/30% before and after) [LY 10.4]. JN 4-for-1 split: total market value stays $200,000 [JN 6.8].
- OS: 200 shares at $10 = $2,000; after a 5% stock dividend, 210 shares are still worth $2,000 (??9.52 each).
- Samsung 2018 50-to-1 split [OS 14.3].
- **Reverse split:** "A primary motivator??is to avoid being delisted??for failure to maintain the exchange's minimum share price" [OS 14.3]. Treat as a distress signal.

**Investor rule:** restate all per-share history (EPS, dividends, book value, price) for splits and stock dividends before computing growth rates, Graham numbers, or PEG.

---

## 7. Items That Bypass Net Income

- **Prior-period adjustments (restatements):** "corrections of errors that appeared on previous periods' financial statements," reported as an adjustment to **beginning retained earnings, net of tax**, so "the adjustment has no effect on current period net income" [OS 14.4]. Clay Corp: $1,000 of understated depreciation, $300 tax effect ??beginning retained earnings ??700.
  - OS (verbatim): "Both shareholders and investors tend to view these with deep suspicion. Many believe corporations are attempting to smooth earnings, hide possible problems, or cover up mistakes." Restatements surged in 2005??6 after SOX.
- **Other comprehensive income (OCI):** "change in equity??from nonowner sources" not in net income; OS lists four components: foreign currency, derivatives, investments, and pensions [OS Ch 2, 14.4]. JN shows available-for-sale gains/losses accumulating in equity until sale [JN 4.10].
- **Appropriated / restricted retained earnings:** restrictions from law or covenants; an appropriation "does not set aside funds" [OS 14.4].
- **Treasury stock reissued below cost** reduces retained earnings directly [OS 14.2].

**Investor test:** over 5??0 years, compare cumulative net income with cumulative comprehensive income and with the change in book value adjusted for dividends, buybacks and share issues. Persistent negative OCI or repeated restatements mean reported earnings overstate economic gains.

---

## 8. Book Value per Share

**LY formulas** [LY 10.5]:
- Book value per preferred share = (Preferred paid-in capital + Dividends in arrears) ÷ Preferred shares outstanding.
- **Book value per common share = [Total equity ??(Preferred paid-in capital + Dividends in arrears)] ÷ Common shares outstanding.**

LY example: total equity $135,000; preferred $10,000 + arrears $5,000; 60,000 common ??preferred $15/share; **common ($135,000 ??$15,000) ÷ 60,000 = $2.00**.

**Market vs book** [LY 10.5]: Corporation A at $40 with $20 book trades at "two times book value"; a higher multiple signals investors expect better profits. LY (verbatim): "Some shares regularly sell for less than their book value??This does not necessarily mean they are a bargain investment. The market price of a share is related to such factors as general economic outlook and perceived potential of the company to generate earnings."

**Big Dog** [LY 12, derived]: book value per share $10.48 ??$11.95 ??$12.31; price-to-book 0.38? ??0.42? ??0.49? with assumed prices $4??6.

**Investor adjustments:** use tangible book (minus goodwill and intangibles) for Graham tests; subtract preferred liquidation value and arrears; consider unrecorded asset values (historical-cost land) and unrecorded liabilities (contingencies) ??see [accounting-foundations.md](./accounting-foundations.md) and [liabilities-debt.md](./liabilities-debt.md).

---

## 9. Earnings per Share

**Definition:** "Earnings per share (EPS) measures the portion of a corporation's profit allocated to each outstanding share of common stock. Many financial analysts believe that EPS is the single most important tool in assessing a stock's market price" [OS 14.5].

$$\text{Basic EPS}=\frac{\text{Net income}-\text{Preferred dividends}}{\text{Weighted average common shares outstanding}}$$

- **Weighted average shares** [OS 14.5]: 600 shares all year plus 1,000 issued April 1 ??600 ? 3/12 + 1,600 ? 9/12 = **1,350** [derived].
- **Common dividends do not reduce the numerator** [OS Sanaron: ($50,000 ??$10,000) ÷ 5,000 = **$8.00**, despite $14,000 of common dividends].
- JN 2019: ($248,000 ??$12,000) ÷ 8,300 = **$28.43**; shares derived as common stock ÷ par [JN 7.3.4].
- LY Big Dog: $1.16 / $1.17 / $1.12 (2024/23/22), flat because income and share count were flat [LY 12.5].
- GAAP requires basic **and diluted** EPS on the face of the income statement; it is the "only ratio that requires such prominent reporting" [OS 14.5]. Diluted EPS covers securities that could dilute (options, convertibles); none of the three books compute it. LY: not required for private companies [LY 11.4].
- GAAP bases EPS on **net income**, not NOPAT or EBITDA, because net income is audited [OS 14.5].

**Continuing vs discontinued operations** [LY 11.4 Toulon]: income from continuing operations $1,983K vs discontinued loss $(147)K net of tax; basic EPS continuing $16.32, discontinued $(1.21). LY: the multi-step format lets investors evaluate "continuing and ongoing operations having a high predictive value separately, compared to non?�operating or unusual items having little predictive value." Discontinued operations require a formal plan to dispose within one year and are shown net of tax.

**Real examples** [OS 14.5]: Microsoft Q1 2018 EPS $0.95 vs $0.85 estimate, stock +3% in hours; Cracker Barrel EPS $6.85 ??$7.91 ??$8.40 ??"Most analysts believe that a consistent improvement in EPS year after year is the indication of continuous improvement in the earning power of a company"; Amazon 1997 EPS ??0.11, yet $5,000 invested grew to nearly $1M ??"EPS does not predict the future."

**EPS limitations listed by OS:** historical; poor cross-industry comparability; moved by share-count changes; "EPS should be a tool used in decision-making, utilized alongside other analytic tools."

**Investor adjustments for normalized EPS:**
1. Use diluted shares; add back nothing for stock compensation (it is a real cost).
2. Use continuing operations; strip gains/losses on disposals, investment gains, debt-extinguishment gains, and one-time items ??but keep recurring "one-time" charges.
3. Deduct preferred dividends including cumulative arrears.
4. Average several years (Graham uses 3-year average EPS).
5. Check EPS growth vs net income growth (buybacks) and vs operating cash flow per share (earnings quality).

---

## 10. P/E and Related Market Measures (detail in [ratio-analysis.md](./ratio-analysis.md))

- **P/E = Market price per share ÷ EPS** [OS 14.5; LY 12.5; JN 7.3.4].
- LY: P/E is "an indicator of the market's expectation of a company's future performance"; Company A at P/E 15 vs B at 8 ??the market "expects Company A to earn relatively more in the future."
- **Caution:** JN calls P/E "The higher the better??the greater the prospect of value growth" [JN 7.3.4]. That is a description of market optimism, **not** a value-investing criterion. For Graham, Lynch and Buffett, a lower P/E for the same quality and growth means a cheaper stock and a larger margin of safety. Cite JN for the formula only.
- **Earnings yield = EPS ÷ Price** (inverse of P/E) for Graham's comparison with bond yields [derived; Big Dog 19.3% / 23.4% / 28.0%].
- **Dividend yield = Dividends per share ÷ Price** [LY 12.5; JN 7.3.4].
- **Payout ratio = Dividends ÷ Net income** [not defined in the books; derived for Big Dog above].
