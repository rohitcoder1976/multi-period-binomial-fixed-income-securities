def compute_cash_account_values(short_rates: list[list[float]]):
    all_values = [[] for _ in range(len(short_rates) + 1)]
    for i in range(len(short_rates) + 1):
        values = []
        if i == 0:
            values.append(1)
        else:
            pass