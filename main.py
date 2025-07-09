from compute.short_rates import compute_short_rates
from compute.zcb import compute_zero_coupon_bond_prices
from compute.forward_contract import compute_forward_contract_price
from lib.out import print_prices

n = 10
r0 = 0.05
u = 1.1
d = 0.9

short_rates = compute_short_rates(n, u, d, r0)
zcb_prices = compute_zero_coupon_bond_prices(maturity=10, short_rates=short_rates, face_value=100)
# print_prices(short_rates)

compute_forward_contract_price(zcb_prices, maturity=5, short_rates=short_rates)