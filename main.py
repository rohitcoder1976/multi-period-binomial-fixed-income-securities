from lib.out import print_prices
from compute.short_rates import compute_short_rates, compute_bdt_short_rates
from compute.zcb import compute_zero_coupon_bond_prices, compute_defaultable_zero_coupon_bond_prices
from compute.forward_contract import compute_forward_contract_price
from compute.futures import compute_futures_price
from compute.options import compute_all_european_call_prices
from compute.swaps import compute_fixed_rate_swap_prices

n = 10
r0 = 0.05
u = 1.1
d = 0.9

# a = [0.0299999810493526, 0.0312017396560733, 0.0323262476252056, 0.0333771067699627, 0.0343570983963617, 0.035269576567804, 0.0330952478291388, 0.0331130028269546, 0.0331104265031268, 0.0330895605370788]
a = [0.0299999863054893, 0.0304045970357651, 0.0306977229476825, 0.0308900981639735, 0.0309914616542764, 0.0310111921440113, 0.0283663677157711, 0.0276686366545309, 0.0269742117973875, 0.0262845408029673]
b= 0.1

short_rates = compute_short_rates(n, u, d, r0)
bdt_short_rates = compute_bdt_short_rates(n=9, a=a, b=b)

zcb_prices = compute_zero_coupon_bond_prices(maturity=10, short_rates=short_rates, face_value=100)

forward_contract_price = compute_forward_contract_price(zcb_prices, maturity=4, short_rates=short_rates)
futures_price = compute_futures_price(zcb_prices=zcb_prices, maturity=4)
call_option_prices = compute_all_european_call_prices(short_rates, maturity=6, prices=zcb_prices, K=80)

swap_prices = compute_fixed_rate_swap_prices(short_rates=short_rates, fixed_rate=0.045, maturity=10, notional_principal=1000000, is_payer=True, starting_time=1)
swaption_prices = compute_all_european_call_prices(prices=swap_prices, K=0, maturity=5, short_rates=short_rates)

defaultable_zcb_prices = compute_defaultable_zero_coupon_bond_prices(maturity=10, short_rates=short_rates, face_value=100, a=0.01, b=1.01, recovery=0.2)
print_prices(swaption_prices)