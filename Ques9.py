# 9.	Triangle Check: Take 3 angles and check if they can form a triangle.
Angle1 = int(input("Enter Angle 1: "))
Angle2 = int(input("Enter Angle 2: "))
Angle3 = int(input("Enter Angle 3: "))
if Angle1 > 0 and Angle2 > 0 and Angle3 > 0:
 if (Angle1+Angle2+Angle3 ==180):
    print("Yes they can form a triangle")
else:
    print("No they cannot form a triangle")
