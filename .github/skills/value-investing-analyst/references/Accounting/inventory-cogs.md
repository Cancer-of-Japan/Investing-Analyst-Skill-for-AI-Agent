# Inventory, Cost of Goods Sold, and Gross Margin

Sources: [OS] OpenStax Ch 6, 10; [LY] Lyryx Ch 5?? & App 6A; [JN] Jonick Ch 3, 4.1. Full citations in [accounting-foundations.md](./accounting-foundations.md).

Inventory is where gross margin is made, and where small accounting choices or count errors move profit one-for-one. Walmart's 2018 inventory was 70% of current assets and 21% of total assets [OS 10.1].

---

## 1. Merchandising Basics and the Multi-Step Income Statement

- **Net sales = Sales ??Sales returns ??Sales discounts** [JN 3.2].
- **Gross profit = Net sales ??COGS**; JN: gross profit "is the same as 'markup.'"
- **Income from operations = Gross profit ??Operating expenses** (selling + administrative).
- LY: "Small fluctuations in the gross profit percentage can have significant effects on the financial performance of a company because the amount of sales and cost of goods sold are often very large in comparison to other income statement items" [LY 5.1].

**LY XYZ Inc. classified multi-step statement (Dec 2023)** [LY 5.5]:

| Line | Amount |
|---|---|
| Sales | $100,000 |
| ??Discounts $1,000, returns $500 | (1,500) |
| **Net sales** | **98,500** |
| COGS | (50,000) |
| **Gross profit** | **48,500** |
| Selling (28,000) + G&A (15,500) | (43,500) |
| **Income from operations** | **5,000** |
| Other: rent revenue 12,000 ??interest 1,500 | 10,500 |
| Income before tax | 15,500 |
| Tax | (3,000) |
| **Net income** | **12,500** |

More than two-thirds of pretax income comes from non-operating rent [derived]. **Always read profit at the operating line before the bottom line.** LY places interest and gains/losses on PP&E in "Other."

**Expense presentation** [LY 5.5]: by **nature** (wages, depreciation, interest) or by **function** (COGS, selling, G&A). If presented by function, nature must also be disclosed, which lets you find depreciation and employee costs.

### Systems, terms, and shrinkage
- **Perpetual** system tracks units and cost in real time; **periodic** uses a Purchases account and a year-end count [JN 3.1, 3.5; LY 5.1]. A physical count is required under both.
- **Periodic COGS** [JN 3.5]: Beginning inventory 10,000 + Purchases 30,000 + Freight-in 5,000 ??Purchase discounts 1,000 ??Purchase returns 2,000 = goods available $42,000; ending count $8,000 ??**COGS $34,000**.
- **Discounts:** "2/10, net 30" = 2% off if paid within 10 days, otherwise full amount in 30 days [JN 3.3.1]. Buyers carry inventory at the cash actually paid.
- **FOB terms** [JN 3.4; OS 10.1]: FOB shipping point ??buyer owns goods in transit and freight is part of inventory cost; FOB destination ??seller owns them and freight is the seller's delivery expense. "Whoever is responsible for absorbing the transportation cost??also owns the merchandise while it is in transit" [JN 4.1.4].
- **Shrinkage** (count below records due to "previous miscounts, loss, or theft") is debited to COGS [JN 3.5.1; LY 5.4]. It lowers gross margin without a separate line. "Further investigation would take place if the amount of the shortage was significant" [JN].
- **Consignment** [OS 10.1]: consigned goods belong to the consignor, not the store holding them.

---

## 2. Cost-Flow Methods

Basic identity: **Beginning inventory + Purchases = Goods available for sale = COGS + Ending inventory** [OS 10.1; LY 6.4].

OS: "a company's cost allocation process represents management's chosen method??which is unrelated to the actual flow of the physical inventory."

| Method | Logic | Typical fit |
|---|---|---|
| Specific identification | Actual cost of each item | "relatively few, expensive items??serial numbers ??for example, motor vehicles" [LY 6.1] |
| FIFO | Oldest costs to COGS | Perishables [LY 6.1] |
| LIFO | Newest costs to COGS | US only; **banned under IFRS** [OS 10.1] |
| Weighted average | Average cost | Commingled goods; "popular in practice because it is easy to calculate" [LY 6.1] |

### Worked examples (rising prices)

**OS Spy Who Loves You Corp. (periodic)** [OS 10.1]: 150 @ $21, 225 @ $27, 210 @ $33 (585 units, $16,155); 300 sold.

| Method | COGS | Ending inventory |
|---|---|---|
| Specific ID | $7,260 | $8,895 |
| FIFO | $7,200 | $8,955 |
| LIFO | $9,360 | $6,795 |
| Weighted average ($27.62) | $8,283 | $7,872 |

**JN main example** (sales $190, goods available $150) [JN 4.1]:

| | Perpetual FIFO | Perpetual LIFO | Perpetual avg | Periodic FIFO | Periodic LIFO | Periodic avg |
|---|---|---|---|---|---|---|
| COGS | $85.00 | $98.00 | $90.70 | $85 | $105 | $95 |
| Gross profit | $105.00 | $92.00 | $99.30 | $105 | $85 | $95 |
| Ending inventory | $65.00 | $52.00 | $58.74 | $65 | $45 | $55 |

"the results for FIFO are the same under the periodic and perpetual inventory systems"; average cost "typically fall[s] between those for LIFO and FIFO" [JN 4.1].

**LY simple example** (units at $1??5, 4 sold at $10): FIFO gross profit $30, specific ID $29, weighted average $28 [LY 6.1].

### Financial-statement effects

| Price environment | FIFO | LIFO |
|---|---|---|
| **Rising costs** | Lower COGS, **higher profit**, higher inventory, higher current ratio, higher taxes | Higher COGS, lower profit, lower inventory, lower taxes |
| Falling costs | Opposite | Opposite |

- LY: "FIFO maximizes net income and ending inventory amounts when costs are rising" [LY 6.2].
- OS: under inflation, FIFO "reflects lower cost of goods sold than the current prices??which produces higher profits" [OS 10.1].
- **LIFO conformity rule:** a US company may use LIFO for tax only if it also uses it in its financial statements [OS 10.1]. About 35??0% of US companies use LIFO, more in oil and gas; repeal would raise an estimated $102B of tax over 2017??026 [OS 10.1].

**Investor adjustments [analyst practice, not stated in the books]:**
- Under FIFO in inflation, part of gross margin is an inventory holding gain that reverses when prices stop rising. Compare gross margin with peers on the same method.
- Under LIFO, the balance sheet understates inventory at current cost; when LIFO layers are liquidated (inventory falls), old low costs flow into COGS and inflate margins temporarily. Read the LIFO reserve note when present.
- Comparing a US LIFO user with an IFRS peer requires converting one to the other's basis.

**Consistency:** methods should not change without a justifiable reason, and a change "requires disclosure in the company's notes" [OS 10.1; LY 6.2]. Different methods may apply to different product lines (LY: Walmart example). **A method change that lifts profit is a red flag.**

---

## 3. Lower of Cost and Market / Net Realizable Value

- LY (IFRS): inventory at the lower of **laid-down cost** (invoice ??discounts + freight-in + insurance in transit + preparation costs) and **net realizable value** [LY 6.3].
- JN (older US terminology): lower of cost or "market," meaning replacement cost or current selling price, applied item by item; justified by **conservatism** [JN 4.1.3].
- Purpose: "to ensure that inventory is not overstated on the balance sheet and that income is not overstated" [LY 6.3].

**Examples**
- JN item-by-item: cost $650 vs LCM $610 ??$40 write-down.
- JN phones: Model #1 kept at cost ($20,000); Model #2 cost $100 but market $60 ??written down to $12,000; total $32,000, not $40,000. "This gives the reader a clearer picture of what the inventory is actually worth."
- LY: unit basis gives a $50 write-down; group basis gives none. **The level at which the test is applied changes the result.**

**Red flags:** large one-time write-downs after years of rising inventory (late recognition); inventory growing in obsolescence-prone industries (electronics, fashion) without write-downs; write-downs reversed later to boost margins (IFRS permits reversal of LCNRV write-downs).

---

## 4. Inventory Errors and Count Problems

**The two-period error** [OS 10.4; LY 6.2]:
- "When cost of goods sold is overstated, inventory and net income are understated. When cost of goods sold is understated, inventory and net income are overstated" [OS].
- "an error in ending inventory carries into the next period, since ending inventory of one period becomes the beginning inventory of the next??Over a two-year period, misstatements of ending inventory will balance themselves out" [OS].

**LY example:** 2022 ending inventory reported $2,000 instead of $1,000.

| | 2022 | 2023 | Two-year total |
|---|---|---|---|
| Gross profit reported | 10,000 | 10,000 | 20,000 |
| Gross profit correct | 9,000 | 11,000 | 20,000 |

**JN count errors** (correct count $20,000) [JN 4.1.4]:

| | Overstated count ($20,500) | Understated count ($19,500) |
|---|---|---|
| Inventory and total assets | Overstated | Understated |
| COGS | Understated | Overstated |
| Net income, retained earnings, equity | **Overstated** | Understated |

**Count rules** [JN 4.1.4]:
- Exclude: goods held on consignment from others; customers' items in for repair; goods set aside for customers who already paid.
- Include: customer returns; goods set aside but unpaid; own goods out on consignment or repair; goods in transit bought FOB shipping point; goods in transit sold FOB destination.

**Common causes of errors** [OS 10.4]: careless counts, FOB ownership mistakes, shrinkage, theft, obsolescence, consigned goods counted as own.

**Inventory fraud red flags (verbatim list)** [OS 10.1]:
- "recording fictitious and nonexistent inventory"
- "manipulation of inventory counts during a facility audit"
- "recording of sales but no recording of purchases"
- "fraudulent inventory capitalization"

Auditors count "on unexpected dates or at unexpected locations" (SAS 99) [OS 10.1]. OS also mentions inflated grain-silo inventory in Texas [OS 8.1].

**Investor implication:** inflating ending inventory raises profit one-for-one this year and reverses next year. A one-year gross-margin jump with rising inventory and falling inventory turnover deserves scrutiny.

---

## 5. Estimating Inventory [LY 6.4]

- **Gross profit method:** Pete's Products, GP 40%, opening $200, purchases $1,100, sales $2,000 ??estimated COGS $1,200, goods available $1,300, **estimated ending inventory $100**. Used after fire/theft or when counts are impractical.
- **Retail method:** at retail, opening $320 + purchases $1,760 = $2,080; less sales $2,000 = $80 at retail; ÷ 160% mark-up = **$50 at cost**. Accurate "provided that no change in the average mark?�up has occurred."
- **Investor use [derived]:** apply the gross-profit method with the company's historical margin to test whether reported ending inventory is plausible. A large gap suggests margin change, write-down timing, or misstatement.

---

## 6. Inventory Ratios

| Ratio | Formula | Interpretation |
|---|---|---|
| **Inventory turnover** | COGS ÷ Average inventory | Higher is better (JN): "the more cash generated??also a measure of a firm's operational performance" |
| **Days' sales in inventory (DSI)** | Average inventory ÷ (COGS ÷ 365) [JN; OS 10.5; LY 12.2]. OS App A uses ending inventory: (Ending inventory ÷ COGS) ? 365 | Lower is better: "less of a need to pay storage, insurance, and other holding costs and less of a chance that inventory on hand will become outdated" [JN] |

**Worked examples**

| Company | Turnover | DSI | Source |
|---|---|---|---|
| LY Company A: $3,000 ÷ $600 | 5? | ??| LY App 6A |
| LY Company B: $3,000 ÷ $1,200 | 2.5? | ??| LY App 6A |
| Jonick 2019: $414,000 ÷ $51,500 | 8.0? | 45.4 days | JN 7.3.4 |
| Big Dog 2024 (avg inv $668, COGS $2,500) | 3.74? [derived] | 97.53 days | LY 12.2 |
| Big Dog 2023 (avg inv $432, COGS $2,150) | 4.98? [derived] | 73.34 days | LY 12.2 |
| Spy Who Loves You, year 1 ??year 2 | 1.19? ??0.84? | ~307 ??~433 days | OS 10.5 |
| Banyan (avg $37,500, COGS $60,000) | 1.6? "very low" | 243 days, "unsustainable long-term" | OS App A |

**Interpretation**
- LY: "The faster a business sells its inventory, the better, because high turnover positively affects liquidity" [LY App 6A].
- OS: "Too little inventory means lost sales opportunities, whereas too much inventory means unproductive investment." DSI "is useful to identify cases of obsolescence, which is especially prevalent in??the technology sector" [OS 10.5].
- LY 12.2: rising DSI usually means poor management, cash tied up, and possible **obsolete** (clothing) or **deteriorating** (perishables) stock. Falling DSI is usually good but risks stock-outs. Ask whether management is deliberately stocking up for growth.
- **Revenue operating cycle = DSI + DSO.** Big Dog: 117.47 ??152.51 days; if suppliers give 60 days, the company "may not be able to pay them" [LY 12.2]. [Analyst extension: subtract days payable outstanding to get the cash conversion cycle.]
- **Inventory growth vs sales growth** is the core screen. Big Dog 2022??024: inventory +131% vs sales +37% [LY, derived]. Lynch makes the same point: inventory growing faster than sales is a red flag (see [lynch.md](../Investors/lynch.md)).

---

## 7. Investor Checklist: Inventory and Gross Margin

1. Identify the cost-flow method, any change, and (for LIFO users) the LIFO reserve and any layer liquidation.
2. Compare inventory growth with sales and COGS growth over 3?? years; compute turnover and DSI vs peers.
3. Separate finished goods, work in progress and raw materials if disclosed: finished goods piling up is worse than raw materials ahead of a known order book.
4. Check write-downs (LCM/LCNRV) and reversals; is the write-down policy applied item-by-item or by group?
5. Track gross margin each year; ask whether changes come from price/mix, input costs, shrinkage, inventory method, or write-down timing.
6. Watch for bill-and-hold, consignment, and in-transit items around period-end.
7. Combine with receivables: DSI + DSO (??DPO) shows how much working capital growth consumes. See [cash-flow-statement.md](./cash-flow-statement.md).
