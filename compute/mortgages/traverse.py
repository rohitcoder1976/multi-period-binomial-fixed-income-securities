from .mortgage_payment import compute_mortgage_payment

def traverse_through_pass_through_mbs_life(n: int, c: float, psa_multiplier: float, initial_principal: float, pass_through_rate: float):
    monthly_interest_rate = c / 12

    outstanding_principal_balance = initial_principal
    mortgage_payment = compute_mortgage_payment(n, monthly_interest_rate, initial_principal)
    total_interest_paid = 0
    total_prepayments_paid = 0

    print("Mortgage payment: " + str(mortgage_payment))
    for i in range(1, n + 1):
        if outstanding_principal_balance <= 0:
            break

        if i <= 30:
            cpr = psa_multiplier * 0.06 * (i / 30)
        else:
            cpr = psa_multiplier * 0.06
            
        smm = 1 - ((1 - cpr) ** (1 / 12))
        interest_paid = (monthly_interest_rate) * outstanding_principal_balance
        principal_paid = mortgage_payment - interest_paid
 
        prepyament = smm * (outstanding_principal_balance - principal_paid)
       
        principal_reduction = principal_paid + prepyament

        if principal_reduction > outstanding_principal_balance:
            principal_reduction = outstanding_principal_balance
            principal_paid = max(0, principal_reduction - interest_paid)

        total_interest_paid += interest_paid * pass_through_rate
        total_prepayments_paid += smm * outstanding_principal_balance * pass_through_rate / c

        outstanding_principal_balance -= principal_reduction

        if i == 10:
            print("Outstanding balance: " + str(outstanding_principal_balance))

        if i < n:
            mortgage_payment = compute_mortgage_payment(n - i, c=monthly_interest_rate, initial_principal=outstanding_principal_balance)


    # print("Outstanding principal balance: " + str(outstanding_principal_balance))
    # print(f"Total interest paid: {str(total_interest_paid)}")
    # print(f"Total prepayments paid: {str(total_prepayments_paid)}")