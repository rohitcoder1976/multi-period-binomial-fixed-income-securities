import math

def compute_short_rates(n: int, u: float, d: float, r0: float):
    all_rates = []
    for i in range(n + 1):
        if i == 0:
            rates = [r0]
        else:
            rates = []
            for j in range(i + 1):
                rates.append(r0 * (u ** j) * (d ** (i - j)))
        all_rates.append(rates)
    return all_rates

def compute_bdt_short_rates(n: int, a: list[float], b: float):
    all_rates = []
    for i in range(n+1):
        rates = []
        for j in range(i+1):
                rates.append(a[i] * math.exp(b * j))
        all_rates.append(rates)
    return all_rates