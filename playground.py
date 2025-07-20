from lib.out import print_prices
from compute.short_rates import compute_short_rates, compute_bdt_short_rates
from compute.zcb import compute_zero_coupon_bond_prices, compute_defaultable_zero_coupon_bond_prices
from compute.forward_contract import compute_forward_contract_price
from compute.futures import compute_futures_price
from compute.options import compute_all_european_call_prices
from compute.swaps import compute_fixed_rate_swap_prices

n = 5
r0 = 0.06
u = 1.25
d = 0.9

short_rates = compute_short_rates(n, u, d, r0)

zcb_prices = compute_zero_coupon_bond_prices(maturity=5, short_rates=short_rates, face_value=100)
swap_prices = compute_fixed_rate_swap_prices(short_rates=short_rates, fixed_rate=0.05, maturity=6, notional_principal=1, is_payer=True)
print_prices(swap_prices)