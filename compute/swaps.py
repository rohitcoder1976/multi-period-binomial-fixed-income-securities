def compute_fixed_rate_swap_prices(
    short_rates: list[list[float]], 
    fixed_rate: float, 
    maturity: int, 
    notional_principal: float,
    is_payer: bool = True,
    starting_time: int = 0,
):
    all_swap_prices = [[] for _ in range(maturity + 1)]
    for r_i in range(maturity):
        i = maturity - 1 - r_i
        prices = []
        if i == maturity - 1: # if near maturity, value of swap is simply discounted cashflow
            for short_rate_j in short_rates[i]:
                if is_payer:
                    cashflow = short_rate_j - fixed_rate
                else:
                    cashflow = fixed_rate - short_rate_j
                price = cashflow * notional_principal / (1 + short_rate_j)
                prices.append(price)
        else:
            for j in range(len(short_rates[i])):
                if i > starting_time:
                    if is_payer:
                        cashflow = short_rates[i][j] - fixed_rate
                    else:
                        cashflow = fixed_rate - short_rates[i][j]
                else:
                    cashflow = 0
                    
                discounted_cashflow = cashflow * notional_principal / (1 + short_rates[i][j])
                # price = discounted, expected sum of future swap prices and cashflows (cashflow one period ahead is deterministic and known, so no need to take expectation for that)
                expected_swap_value = ((0.5 * all_swap_prices[i+1][j]) + (0.5 * all_swap_prices[i+1][j+1])) / (1 + short_rates[i][j])
                prices.append(expected_swap_value + discounted_cashflow)
        all_swap_prices[i] = prices
    return all_swap_prices