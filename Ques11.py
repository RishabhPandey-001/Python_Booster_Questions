# 11.	Simple Interest: Calculate simple interest given principal, rate, and time.
def SimpleInterest(P, R, T):
    si = (P * R * T)/100
    return si
try:
    p = float(input("Enter the Principal amount (₹): "))
    r = float(input("Enter the Rate of interest (%): "))
    t = float(input("Enter the Time period (in years): "))

    interest = SimpleInterest(p ,r,t)
    print(f"Simple Interest = ₹{interest:.2f}")
except ValueError:
    print("Please enter valid numeric values.")