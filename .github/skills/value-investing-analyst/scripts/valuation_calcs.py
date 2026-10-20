#!/usr/bin/env python3
"""Deterministic valuation formulas for the value-investing-analyst skill.

Every formula here is cited to its source in references/Investors/*.md so the
numbers match the doctrine the skill analyzes against. This script does the
arithmetic only; judgment (which inputs to use, how much to trust them,
whether a lens applies at all) stays with the model.

Usage (as a library):
    from valuation_calcs import graham_number, margin_of_safety, ...

Usage (CLI, one calc at a time):
    python valuation_calcs.py graham_number --eps 5.37 --bvps 34.3
    python valuation_calcs.py owner_earnings --net_income 100 --dep_amort 20 --maintenance_capex 30
    python valuation_calcs.py --help
"""

from __future__ import annotations

import argparse
import math
import sys
from dataclasses import dataclass


# ---------------------------------------------------------------------------
# Graham (references/Investors/graham.md)
# ---------------------------------------------------------------------------

def graham_number(eps_3yr_avg: float, bvps: float) -> float:
    """Graham Number = sqrt(22.5 * EPS_3yr_avg * BVPS).

    Source: graham.md "Derived Graham Number... (max price that passes test 7
    with EPS on a 3-yr avg basis)." Ch.14 criteria: P/E <= 15x and P/B <= 1.5x,
    combined as P/E * P/B <= 22.5.

    Returns the max price passing Graham's Ch.14 moderate P/E + moderate P/B
    screen simultaneously. Undefined (raises) if EPS or BVPS <= 0 — Graham's
    screen assumes positive earnings and book value.
    """
    if eps_3yr_avg <= 0 or bvps <= 0:
        raise ValueError(
            "Graham Number requires positive EPS (3-yr avg) and positive BVPS; "
            "do not calculate for loss-making or negative-book-value companies."
        )
    return math.sqrt(22.5 * eps_3yr_avg * bvps)


def graham_growth_value(normalized_eps: float, growth_pct: float) -> float:
    """V = E_normal * (8.5 + 2g).

    Source: graham.md "Growth-stock valuation formula [verified]: V = E_normal
    x (8.5 + 2g). 8.5 = P/E for zero growth; g = expected annual growth over
    the next 7-10 years."

    growth_pct is a whole number (e.g. 12 for 12%), not a decimal.
    Graham explicitly warns this formula is illustrative and can overstate
    value; never rely on it alone (see graham.md Ch.11 growth formula note).
    """
    return normalized_eps * (8.5 + 2 * growth_pct)


def ncav_per_share(current_assets: float, total_liabilities: float,
                    preferred_stock: float, shares_outstanding: float) -> float:
    """Net Current Asset Value per share = (current assets - all liabilities
    - preferred) / shares outstanding.

    Source: graham.md "Net-current-asset stocks ('net-nets'): buy a
    diversified group ... below NCAV." Classic stricter rule: buy only at
    <= 2/3 of NCAV per share.
    """
    if shares_outstanding <= 0:
        raise ValueError("shares_outstanding must be positive")
    return (current_assets - total_liabilities - preferred_stock) / shares_outstanding


def earnings_yield(eps: float, price: float) -> float:
    """Earnings yield = EPS / Price (= 1 / P/E).

    Source: graham.md Ch.20 margin of safety: "earning power (earnings yield
    = 1 / P/E) well above the bond rate."
    """
    if price <= 0:
        raise ValueError("price must be positive")
    return eps / price


def margin_of_safety(conservative_value: float, price: float) -> float:
    """Margin of safety = (conservative value - price) / conservative value.

    Source: SKILL.md Step 8. Guidelines: defensive >= 25-33%; secondary/
    less-proven companies >= 33%; wonderful businesses may be bought near fair
    value if the moat is durable.
    """
    if conservative_value <= 0:
        raise ValueError("conservative_value must be positive")
    return (conservative_value - price) / conservative_value


# ---------------------------------------------------------------------------
# Lynch (references/Investors/lynch.md)
# ---------------------------------------------------------------------------

def peg_ratio(pe_ratio: float, growth_pct: float) -> float:
    """PEG = P/E / growth rate (growth_pct as a whole number, e.g. 15 not 0.15).

    Source: lynch.md "P/E vs growth [verified]: P/E = growth rate is fair.
    P/E = 1/2 of growth = very positive; 2x growth = very negative."
    Approx bands: ~1 fair, ~0.5 very attractive, >=2 very unattractive.

    Do not use for negative or highly cyclical earnings (lynch.md warns P/E
    at peak cyclical earnings is a trap).
    """
    if growth_pct <= 0:
        raise ValueError(
            "PEG is not meaningful for zero/negative growth; do not use for "
            "cyclicals at peak earnings (see lynch.md cyclical notes)."
        )
    return pe_ratio / growth_pct


def dividend_adjusted_ratio(growth_pct: float, dividend_yield_pct: float,
                             pe_ratio: float) -> float:
    """(growth% + dividend yield%) / P/E.

    Source: lynch.md "Dividend-adjusted ratio [verified]: (Long-term growth %
    + dividend yield %) / P/E. <1 poor, 1.5 okay, >=2 what you want.
    15% + 3% / 6 = 3 (fabulous)."
    """
    if pe_ratio <= 0:
        raise ValueError("P/E ratio must be positive")
    return (growth_pct + dividend_yield_pct) / pe_ratio


def net_cash_per_share(cash_and_securities: float, long_term_debt: float,
                        shares_outstanding: float) -> float:
    """Net cash per share = (cash + securities - long-term debt) / shares.

    Source: lynch.md "Cash position: Net cash (cash + securities - long-term
    debt) per share lowers the real price." Ford 1987 example in source.
    """
    if shares_outstanding <= 0:
        raise ValueError("shares_outstanding must be positive")
    return (cash_and_securities - long_term_debt) / shares_outstanding


def pe_ex_cash(price: float, net_cash_per_share_value: float, eps: float) -> float:
    """P/E ex-cash = (Price - net cash per share) / EPS.

    Source: lynch.md cash position discussion (Ford 1987: "the auto business
    cost ~$5.10 for ~$7 of EPS" after backing out net cash/share).
    """
    if eps <= 0:
        raise ValueError("EPS must be positive to compute a P/E")
    return (price - net_cash_per_share_value) / eps


# ---------------------------------------------------------------------------
# Buffett (references/Investors/buffett.md)
# ---------------------------------------------------------------------------

def owner_earnings(net_income: float, dep_amort_noncash: float,
                    maintenance_capex: float, extra_working_capital: float = 0.0) -> float:
    """Owner earnings = net income + D&A (and other non-cash charges)
    - average annual maintenance capex (- extra working capital required).

    Source: buffett.md "Owner earnings [verified]: (a) reported earnings +
    (b) depreciation, depletion, amortization, and certain other non-cash
    charges - (c) the average annual capital expenditures ... needed to fully
    maintain long-term competitive position and unit volume (plus any extra
    working capital required)."

    maintenance_capex is a judgment estimate (Buffett: "(c) is a guess, but
    it's the relevant figure. Better vaguely right than precisely wrong.") —
    do not pass total capex if growth capex is mixed in; separate them first.
    Never use EBITDA as a substitute (buffett.md: "EBITDA is a dangerous
    fiction").
    """
    return net_income + dep_amort_noncash - maintenance_capex - extra_working_capital


@dataclass
class DCFSensitivity:
    low: float
    base: float
    high: float


def owner_earnings_dcf(owner_earnings_ttm: float, growth_pct: float,
                        discount_rate_pct: float, terminal_growth_pct: float,
                        years: int = 10) -> float:
    """Simple two-stage DCF on owner earnings: explicit growth for `years`,
    then a Gordon-growth terminal value at terminal_growth_pct.

    Source: buffett.md "Intrinsic value = discounted value of the cash that
    can be taken out of a business during its remaining life." SKILL.md
    Step 5: "cap mature terminal growth below long-run nominal economic
    growth... show low/base/high sensitivity" (see owner_earnings_dcf_range).

    All rate inputs are whole-number percentages (e.g. 8 for 8%), not decimals.
    discount_rate_pct must exceed terminal_growth_pct or the terminal value
    is undefined (divide-by-zero or negative denominator).
    """
    if discount_rate_pct <= terminal_growth_pct:
        raise ValueError(
            "discount_rate_pct must exceed terminal_growth_pct, else terminal "
            "value is undefined. Buffett: discount rate should be at least "
            "the long-term government bond yield plus a safety cushion."
        )
    g = growth_pct / 100.0
    r = discount_rate_pct / 100.0
    tg = terminal_growth_pct / 100.0

    pv_explicit = 0.0
    oe = owner_earnings_ttm
    for year in range(1, years + 1):
        oe *= (1 + g)
        pv_explicit += oe / ((1 + r) ** year)

    terminal_oe = oe * (1 + tg)
    terminal_value = terminal_oe / (r - tg)
    pv_terminal = terminal_value / ((1 + r) ** years)

    return pv_explicit + pv_terminal


def owner_earnings_dcf_range(owner_earnings_ttm: float,
                              growth_low_base_high: tuple[float, float, float],
                              discount_rate_pct: float,
                              terminal_growth_pct: float,
                              years: int = 10) -> DCFSensitivity:
    """Low/base/high intrinsic value range by varying the growth assumption.

    Source: SKILL.md Step 5 requires showing low/base/high sensitivity rather
    than a single point estimate ("A precise output from uncertain inputs is
    not a precise valuation" — Operating Rules).
    """
    low_g, base_g, high_g = growth_low_base_high
    return DCFSensitivity(
        low=owner_earnings_dcf(owner_earnings_ttm, low_g, discount_rate_pct, terminal_growth_pct, years),
        base=owner_earnings_dcf(owner_earnings_ttm, base_g, discount_rate_pct, terminal_growth_pct, years),
        high=owner_earnings_dcf(owner_earnings_ttm, high_g, discount_rate_pct, terminal_growth_pct, years),
    )


def dollar_test(market_value_added: float, retained_earnings_cumulative: float) -> float:
    """The '$1 test': market value created per $1 retained.

    Source: buffett.md checklist "Rational capital allocation: retained
    earnings pass the $1 test?" — has each $1 retained created >= $1 of
    market value over 5-10 years? Returns the ratio; >= 1.0 passes.
    """
    if retained_earnings_cumulative <= 0:
        raise ValueError("retained_earnings_cumulative must be positive")
    return market_value_added / retained_earnings_cumulative


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("graham_number", help="sqrt(22.5 * EPS_3yr_avg * BVPS)")
    p.add_argument("--eps", type=float, required=True, help="3-year average EPS")
    p.add_argument("--bvps", type=float, required=True, help="Book value per share")

    p = sub.add_parser("graham_growth_value", help="V = E * (8.5 + 2g)")
    p.add_argument("--eps", type=float, required=True, help="Normalized EPS")
    p.add_argument("--growth", type=float, required=True, help="Expected growth %% (e.g. 12)")

    p = sub.add_parser("ncav_per_share", help="(current assets - all liabilities - preferred) / shares")
    p.add_argument("--current_assets", type=float, required=True)
    p.add_argument("--total_liabilities", type=float, required=True)
    p.add_argument("--preferred", type=float, default=0.0)
    p.add_argument("--shares", type=float, required=True)

    p = sub.add_parser("earnings_yield", help="EPS / Price")
    p.add_argument("--eps", type=float, required=True)
    p.add_argument("--price", type=float, required=True)

    p = sub.add_parser("margin_of_safety", help="(value - price) / value")
    p.add_argument("--value", type=float, required=True)
    p.add_argument("--price", type=float, required=True)

    p = sub.add_parser("peg_ratio", help="P/E / growth%%")
    p.add_argument("--pe", type=float, required=True)
    p.add_argument("--growth", type=float, required=True)

    p = sub.add_parser("dividend_adjusted_ratio", help="(growth%% + yield%%) / P/E")
    p.add_argument("--growth", type=float, required=True)
    p.add_argument("--yield_pct", type=float, required=True)
    p.add_argument("--pe", type=float, required=True)

    p = sub.add_parser("net_cash_per_share", help="(cash+securities - LT debt) / shares")
    p.add_argument("--cash", type=float, required=True)
    p.add_argument("--debt", type=float, required=True)
    p.add_argument("--shares", type=float, required=True)

    p = sub.add_parser("pe_ex_cash", help="(Price - net cash/share) / EPS")
    p.add_argument("--price", type=float, required=True)
    p.add_argument("--net_cash_per_share", type=float, required=True)
    p.add_argument("--eps", type=float, required=True)

    p = sub.add_parser("owner_earnings", help="NI + D&A - maintenance capex - extra WC")
    p.add_argument("--net_income", type=float, required=True)
    p.add_argument("--dep_amort", type=float, required=True)
    p.add_argument("--maintenance_capex", type=float, required=True)
    p.add_argument("--extra_working_capital", type=float, default=0.0)

    p = sub.add_parser("owner_earnings_dcf", help="Two-stage DCF on owner earnings")
    p.add_argument("--owner_earnings", type=float, required=True, dest="oe")
    p.add_argument("--growth", type=float, required=True)
    p.add_argument("--discount_rate", type=float, required=True)
    p.add_argument("--terminal_growth", type=float, required=True)
    p.add_argument("--years", type=int, default=10)

    p = sub.add_parser("dollar_test", help="market value added / cumulative retained earnings")
    p.add_argument("--market_value_added", type=float, required=True)
    p.add_argument("--retained_earnings", type=float, required=True)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    try:
        if args.command == "graham_number":
            result = graham_number(args.eps, args.bvps)
        elif args.command == "graham_growth_value":
            result = graham_growth_value(args.eps, args.growth)
        elif args.command == "ncav_per_share":
            result = ncav_per_share(args.current_assets, args.total_liabilities, args.preferred, args.shares)
        elif args.command == "earnings_yield":
            result = earnings_yield(args.eps, args.price)
        elif args.command == "margin_of_safety":
            result = margin_of_safety(args.value, args.price)
        elif args.command == "peg_ratio":
            result = peg_ratio(args.pe, args.growth)
        elif args.command == "dividend_adjusted_ratio":
            result = dividend_adjusted_ratio(args.growth, args.yield_pct, args.pe)
        elif args.command == "net_cash_per_share":
            result = net_cash_per_share(args.cash, args.debt, args.shares)
        elif args.command == "pe_ex_cash":
            result = pe_ex_cash(args.price, args.net_cash_per_share, args.eps)
        elif args.command == "owner_earnings":
            result = owner_earnings(args.net_income, args.dep_amort, args.maintenance_capex, args.extra_working_capital)
        elif args.command == "owner_earnings_dcf":
            result = owner_earnings_dcf(args.oe, args.growth, args.discount_rate, args.terminal_growth, args.years)
        elif args.command == "dollar_test":
            result = dollar_test(args.market_value_added, args.retained_earnings)
        else:
            parser.error(f"unknown command {args.command}")
            return 2
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
