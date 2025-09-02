# 13.	Divisibility Check: Check if a number is divisible by 3 & 6.
def Divisibility_check(num):
    if num % 3 ==0 and num % 6 == 0:
        print("Number is divisible by both 3 and 6")
    elif num % 3 == 0:
      print("Number is divisible by 3")
    elif num % 6 == 0:
      print("Number is divisible by 6")  
    else:
       print("Number is not divisible by 3 or 6")

try:
    number = int(input("Enter number: "))
    Divisibility_check(number)
except ValueError:
    print("Please enter a valid integer!")   


       

