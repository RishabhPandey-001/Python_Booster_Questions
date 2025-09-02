# Armstrong numbers between 100 and 1000
print("Armstrong numbers between 100 and 1000:")

for num in range(100, 1000):
    # Extract each digit
    digit1 = num // 100        # Hundreds digit
    digit2 = (num // 10) % 10  # Tens digit
    digit3 = num % 10          # Ones digit
    
    # Calculate sum of cubes of each digit
    sum_of_cubes = digit1**3 + digit2**3 + digit3**3
    
    # Check if it's an Armstrong number
    if num == sum_of_cubes:
        print(num)



