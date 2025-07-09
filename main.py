from lib.out import print_prices
from compute.short_rates import compute_short_rates
from compute.zcb import compute_zero_coupon_bond_prices
from compute.forward_contract import compute_forward_contract_price
from compute.futures import compute_futures_price
from compute.options import compute_all_european_call_prices

n = 10
r0 = 0.05
u = 1.1
d = 0.9

short_rates = compute_short_rates(n, u, d, r0)
zcb_prices = compute_zero_coupon_bond_prices(maturity=10, short_rates=short_rates, face_value=100)

forward_contract_price = compute_forward_contract_price(zcb_prices, maturity=4, short_rates=short_rates)
futures_price = compute_futures_price(zcb_prices=zcb_prices, maturity=4)
call_option_prices = compute_all_european_call_prices(short_rates, maturity=6, prices=zcb_prices, K=80)

print_prices(call_option_prices)