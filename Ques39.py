# 39.	Reverse Any Number: Reverse digits of any number.
num = int(input("Enter a number: "))
is_negative = num < 0
num = abs(num)
reversed_num = int(str(num)[::-1])
if is_negative:
    reversed_num = -reversed_num

print("Reversed number:", reversed_num)






#     num = int(input("Enter a number: "))

# is_negative = num < 0
# num = abs(num)

# reversed_num = 0
# while num > 0:
#     digit = num % 10
#     reversed_num = reversed_num * 10 + digit
#     num = num // 10

# if is_negative:
#     reversed_num = -reversed_num

# print("Reversed number:", reversed_num)
