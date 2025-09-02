# 1.	Find the Oldest Age: User will input 3 ages. Find the oldest one
print("Enter the Ages")
Age1 = int(input("Enter the First age: "))
Age2 = int(input("Enter the second age: "))
Age3 = int(input("Enter the third age: "))
if Age1>Age2 and Age1>Age3:
    print("Age1 is oldest among all")
elif Age2>Age1 and Age2 > Age3:
    print("Age2 is oldest among all")
else:
    print("Age3 is oldest among all")    
