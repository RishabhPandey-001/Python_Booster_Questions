# 25.	Factorial of a Number: Compute factorial.
def factorial(num):
    if num<0:
       print("The factorial of negative number is not exist")
    elif num ==1 or num == 0:
        return 1
    else: 
     return num * factorial(num - 1)
            
fact = int(input("Enter the number: "))
result = factorial(fact)
print(f"The factorial of {fact} is {result}")

