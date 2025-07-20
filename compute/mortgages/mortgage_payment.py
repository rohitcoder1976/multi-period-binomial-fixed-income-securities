def compute_mortgage_payment(n: int, c: float, initial_principal: float):
    payment = (c * ((1 + c) ** n)) / (((1 + c) ** n) - 1) * initial_principal
    return payment