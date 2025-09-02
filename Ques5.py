# 5.	Reverse a 4-Digit Number: Reverse a 4-digit number and check if it's equal to the original.
Number = int(input("Enter a 4 digit Number: "))
if 1000<= Number <=9999:
    reversed_num = int(str(Number)[::-1])
    print(f"Reversed Number: {reversed_num}")

    if Number == reversed_num:
        print("Yes the reversed digit is Equal")
    else:
        print("No the digits are not equal")
else: 
     print("Please enter a valid 4-digit number.")
           