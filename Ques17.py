# 17.	Sum of Squares of Digits: Take 3 digits and add their squares.
Digit_First = int(input("Enter digit First: "))
Digit_Second = int(input("Enter digit Second: "))
Digit_Third = int(input("Enter digit third: "))
print("Your digits are:",Digit_First,Digit_Second,Digit_Third)
Square_first = Digit_First**2
Square_second = Digit_Second**2
Square_third = Digit_Third**2
sum_of_squares = Square_first + Square_second + Square_third
print("The sum of squares of digits is: ",sum_of_squares)