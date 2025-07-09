import math

def compute_futures_price(zcb_prices: list[list[float]], maturity: int):
    price = 0
    for i in range(maturity + 1):
        price += math.comb(maturity, i) * zcb_prices[maturity][i] * (0.5 ** maturity)
    return price