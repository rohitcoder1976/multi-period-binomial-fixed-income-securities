from typing import Callable
from .zcb import traverse_to_zcb_price

def compute_forward_contract_price(zcb_prices: list[list[float]], maturity: int, short_rates: list[list[float]]):
    # compute the risk-neutral expectation of the ratio of zero coupon bond price at time t to value of cash account at time t
    all_expected_ratios = [[] for _ in range(maturity + 1)]
    cash_account_info: list[dict] = []
    
    # traverse each path through the short rate binomial lattice 
    # and compute the value of Bt (multiplied by risk-neutral probabilities) at each node    
    def add_value(values: dict):
        cash_account_info.append(values)

    traverse_and_compute_cash_account_values(maturity=maturity, short_rates=short_rates, add_value=add_value)

    expected_zcb_to_ca_ratio = 0
    for i in cash_account_info:
        zt = traverse_to_zcb_price(zcb_prices=zcb_prices, u=i["u"], d=i["d"])
        # the risk-neutral probability is definitely off
        expected_zcb_to_ca_ratio += (0.5 ** (maturity)) * (zt / i["value"])

    expected_one_over_ca = 0
    for i in cash_account_info:
        expected_one_over_ca += (0.5 ** (maturity)) * (1 / i["value"])
    
    return expected_zcb_to_ca_ratio / expected_one_over_ca


def traverse_and_compute_cash_account_values(
    maturity: int,
    short_rates: list[list[float]], 
    i: int = 0, 
    j: int = 0, 
    u: int = 0,
    d: int = 0,
    value: float = 1,
    add_value=Callable[[dict], None]
):
    short_rate = short_rates[i][j]
    if i == maturity: # if at last node, return information
        add_value({
            "u": u,
            "d": d,
            "value": value
        })
    else:
        traverse_and_compute_cash_account_values(maturity, short_rates=short_rates, i=i+1, j=j+1, value=value*(1+short_rate), add_value=add_value, u=u+1, d=d)
        traverse_and_compute_cash_account_values(maturity, short_rates=short_rates, i=i+1, j=j, value=value*(1+short_rate), add_value=add_value, u=u, d=d+1)

