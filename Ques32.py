# 32.	LCM of Two Numbers: Find the least common multiple.
def find_lcm(x, y):
    if(x>y):
        greater = x
    else:
        greater = y
    while(True):
        if (greater % x == 0)  and (greater % y ==0):
            lcm = greater
            break
        else:
            greater += 1
    return lcm        

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

print("The LCM of {} and {} is {}".format(num1, num2,find_lcm(num1, num2)))
