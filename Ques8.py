# 8.	Euclidean Distance: Find the distance between two coordinates.
import math
def EuclideanDistance(x1,y1,x2,y2):
    distance = math.sqrt((x2-x1)**2 +(y2 - y1)**2)
    return distance
x1 = float(input("Enter X1: "))
x2 = float(input("Enter X2: "))
y1 = float(input("Enter y1: "))
y2 = float(input("Enter y2: "))    

distance = EuclideanDistance(x1, y1, x2, y2)
print(f"The Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is: {distance}")