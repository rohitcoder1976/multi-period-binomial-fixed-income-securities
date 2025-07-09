def compute_zero_coupon_bond_prices(maturity: int, short_rates: list[list[float]], face_value: int):
    all_prices = [[] for _ in range(maturity + 1)]
    for r_i in range(maturity + 1):
        i = maturity - r_i
        prices = []
        if i == maturity:
            prices = [face_value] * (maturity + 1)
        else:
            for j in range(i + 1):
                price = (1 / (1 + short_rates[i][j])) * (0.5 * all_prices[i+1][j] + 0.5 * all_prices[i+1][j + 1])
                prices.append(price)
        all_prices[i] = prices
    return all_prices

def traverse_to_zcb_price(zcb_prices: list[list[float]], u: int, d: int) -> float:
    time = 0
    state = 0
    for _ in range(u):
        time += 1
        state += 1
    
    for _ in range(d):
        time += 1
    return zcb_prices[time][state]