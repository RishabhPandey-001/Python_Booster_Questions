# 18.	Armstrong Number Check: Check if a number is an Armstrong number.
num = int(input("Enter the Number: "))
order = len(str(num))
sum_of_powers = 0
temp = num
while temp>0:
    digits = temp % 10
    sum_of_powers += digits ** order
    temp //= 10
if num == sum_of_powers:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")    