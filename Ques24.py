# 24.	Multiply Without * Operator: Multiply two numbers without using *.
def multiply(a, b):
    
    negative = False
    if a < 0 and b > 0:
        a = -a
        negative = True
    elif b < 0 and a > 0:
        b = -b
        negative = True
    elif a < 0 and b < 0:
        a = -a
        b = -b

    result = 0
    for _ in range(b):
        result += a

    return -result if negative else result

value1 = int(input("Enter the value of a: "))
value2 = int(input("Enter the value of b: "))

print(multiply(value1,value2)) 

