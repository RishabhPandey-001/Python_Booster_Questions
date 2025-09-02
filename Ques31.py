# 31.	HCF of Two Numbers: Find the highest common factor
def find_hcf(x, y):
    hcf = 1
    for i in range(1, min(x,y)+1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"The HCF of {num1} and {num2} is {find_hcf(num1, num2)}")
