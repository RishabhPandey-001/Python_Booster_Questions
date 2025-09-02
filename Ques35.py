# 35.	Compound Interest: Calculate compound interest.
# Program to calculate compound interest

def compound_interest(P, r, t):
    A = P * (1 + r / 100) ** t
    CI = A - P
    return CI

P = float(input("Enter the principal amount (P): "))
r = float(input("Enter the annual interest rate (r): "))
t = float(input("Enter the time in years (t): "))


CI = compound_interest(P, r, t)
print(f"Compound Interest after {t} years = {CI:.2f}")
