# 38.	Factors of a Number: Print all factors.
num = int(input("Enter the number: "))
print(f"factors of {num} are: ")
for i in range(1, num+1):
    if num % i ==0:
        print(i)