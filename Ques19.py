# Narcissistic Number Check for 4-digit number
num = int(input("Enter a 4-digit number: "))

# Check if the number is 4 digits
if 1000 <= num <= 9999:
    sum_of_powers = 0
    temp = num

    while temp > 0:
        digit = temp % 10       # Get last digit
        sum_of_powers += digit ** 4  # Raise to power 4 and add to sum
        temp //= 10             # Remove last digit

    if num == sum_of_powers:
        print(num, "is a narcissistic number.")
    else:
        print(num, "is not a narcissistic number.")

else:
    print("Please enter a valid 4-digit number.")
