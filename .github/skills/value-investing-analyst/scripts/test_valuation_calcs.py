#!/usr/bin/env python3
"""Self-check for valuation_calcs.py against worked examples cited in the
references (references/Investors/graham.md, lynch.md, buffett.md).

Run: python test_valuation_calcs.py
"""

import math

from valuation_calcs import (
    dividend_adjusted_ratio,
    dollar_test,
    earnings_yield,
    graham_growth_value,
    graham_number,
    margin_of_safety,
    ncav_per_share,
    net_cash_per_share,
    owner_earnings,
    owner_earnings_dcf,
    pe_ex_cash,
    peg_ratio,
)


def assert_close(actual: float, expected: float, label: str, tol: float = 1e-6) -> None:
    assert math.isclose(actual, expected, rel_tol=tol), f"{label}: expected {expected}, got {actual}"
    print(f"ok  {label} = {actual}")


def main() -> None:
    # Graham Number: textbook example "9x earnings and 2.5x book qualifies"
    # i.e. P/E=9, P/B=2.5 -> P/E*P/B=22.5 exactly at the boundary.
    # With EPS=1, BVPS such that P/B=2.5 at price=9 -> BVPS = 9/2.5 = 3.6
    gn = graham_number(eps_3yr_avg=1.0, bvps=3.6)
    assert_close(gn, 9.0, "graham_number boundary case (P/E=9,P/B=2.5->price=9)")

    # Graham growth formula: V = E * (8.5 + 2g), g=10 -> V = E * 28.5
    v = graham_growth_value(normalized_eps=2.0, growth_pct=10)
    assert_close(v, 2.0 * 28.5, "graham_growth_value g=10%")

    # NCAV: current assets 100, total liabilities 40, preferred 0, 10 shares
    # -> NCAV/share = 6.0
    ncav = ncav_per_share(current_assets=100, total_liabilities=40, preferred_stock=0, shares_outstanding=10)
    assert_close(ncav, 6.0, "ncav_per_share")

    # Earnings yield: EPS 5, price 50 -> 10%
    ey = earnings_yield(eps=5, price=50)
    assert_close(ey, 0.10, "earnings_yield")

    # Margin of safety: value 100, price 70 -> 30%
    mos = margin_of_safety(conservative_value=100, price=70)
    assert_close(mos, 0.30, "margin_of_safety")

    # Lynch PEG: "12% grower at P/E 6 attractive" -> PEG 0.5
    peg = peg_ratio(pe_ratio=6, growth_pct=12)
    assert_close(peg, 0.5, "peg_ratio (12% grower, P/E 6)")

    # Lynch PEG: "6% grower at P/E 12 unattractive" -> PEG 2.0
    peg2 = peg_ratio(pe_ratio=12, growth_pct=6)
    assert_close(peg2, 2.0, "peg_ratio (6% grower, P/E 12)")

    # Lynch dividend-adjusted ratio worked example: 15% + 3% / 6 = 3 (fabulous)
    dar = dividend_adjusted_ratio(growth_pct=15, dividend_yield_pct=3, pe_ratio=6)
    assert_close(dar, 3.0, "dividend_adjusted_ratio (15%+3%)/6")

    # Net cash per share + P/E ex-cash, loosely following the Ford 1987 shape
    # (cash 1630, debt 0, 100 shares -> net cash/share 16.30)
    ncps = net_cash_per_share(cash_and_securities=1630, long_term_debt=0, shares_outstanding=100)
    assert_close(ncps, 16.30, "net_cash_per_share")
    pe_x = pe_ex_cash(price=38, net_cash_per_share_value=16.30, eps=7)
    assert_close(pe_x, (38 - 16.30) / 7, "pe_ex_cash")

    # Owner earnings: NI 100, D&A 20, maintenance capex 30, extra WC 5 -> 85
    oe = owner_earnings(net_income=100, dep_amort_noncash=20, maintenance_capex=30, extra_working_capital=5)
    assert_close(oe, 85.0, "owner_earnings")

    # Owner earnings DCF: sanity check it's positive and terminal > explicit
    # when growth is modest and discount > terminal growth
    dcf_value = owner_earnings_dcf(owner_earnings_ttm=100, growth_pct=5, discount_rate_pct=9, terminal_growth_pct=2, years=10)
    assert dcf_value > 0, "owner_earnings_dcf should be positive for sane inputs"
    print(f"ok  owner_earnings_dcf sanity = {dcf_value:.2f}")

    # Dollar test: $150 market value added per $100 retained -> 1.5 (passes)
    dt = dollar_test(market_value_added=150, retained_earnings_cumulative=100)
    assert_close(dt, 1.5, "dollar_test")

    # Error-path checks (bad inputs should raise, not silently return garbage)
    try:
        graham_number(eps_3yr_avg=-1, bvps=10)
        raise AssertionError("graham_number should reject negative EPS")
    except ValueError:
        print("ok  graham_number rejects negative EPS")

    try:
        peg_ratio(pe_ratio=10, growth_pct=0)
        raise AssertionError("peg_ratio should reject zero growth")
    except ValueError:
        print("ok  peg_ratio rejects zero growth")

    try:
        owner_earnings_dcf(owner_earnings_ttm=100, growth_pct=5, discount_rate_pct=2, terminal_growth_pct=3, years=10)
        raise AssertionError("owner_earnings_dcf should reject discount <= terminal growth")
    except ValueError:
        print("ok  owner_earnings_dcf rejects discount_rate <= terminal_growth")

    print("\nAll checks passed.")


if __name__ == "__main__":
    main()
