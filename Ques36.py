# 36. compute n + nn + nnn for a given integer n.
n = input("Enter the single-digit value of n: ")

if n.isdigit() and len(n) == 1:
    n = int(n)
    result = n + int(str(n) * 2) + int(str(n) * 3)
    print(f"Result: {result}")
else:
    print("Please enter a valid single-digit number.")
