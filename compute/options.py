import math

def compute_all_call_payoffs(n: int, prices: list[list[float]], K: float):
    all_call_payoffs = []
    for i in range(n + 1):
        call_payoffs = []
        for j in range(i + 1):
            call_payoffs.append(max(prices[i][j] - K, 0))
        all_call_payoffs.append(call_payoffs)
    return all_call_payoffs

def compute_all_european_call_prices(short_rates: list[list[float]], maturity: int, prices: list[list[float]], K: float):
    all_call_payoffs = compute_all_call_payoffs(n=maturity, prices=prices, K=K)
    all_call_prices = [[] for _ in range(maturity + 1)]
    for r_i in range(maturity + 1):
        i = maturity - r_i
        if i == maturity: # if at the last step, the prices are the payoffs (arbitrage-free pricing)
            all_call_prices[i] = all_call_payoffs[i]
        else:
            call_prices = []
            for j in range(i + 1):
                price = (1/(1 + short_rates[i][j])) * ((0.5 * all_call_prices[i + 1][j + 1]) + 0.5 * all_call_prices[i + 1][j])
                call_prices.append(price)
            all_call_prices[i] = call_prices
    return all_call_prices
