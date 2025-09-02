# 23.	Sum of First N Numbers: Find sum (e.g., n=10 → 55).
def sum_of_First_N_numbers(num):
    sum = num * (num + 1) // 2
    return sum

number = int(input("Enter the Number: "))
result = sum_of_First_N_numbers(number)
print(f"The sum of first {number} natural numbers is: {result}")
