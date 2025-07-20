from compute.mortgages.mortgage_payment import compute_mortgage_payment
from compute.mortgages.traverse import traverse_through_pass_through_mbs_life

mortgage_payment = compute_mortgage_payment(30*12, 0.05/12, 400000)
traverse_through_pass_through_mbs_life(n=240, c=0.06, psa_multiplier=1, initial_principal=40000000, pass_through_rate=0.05)