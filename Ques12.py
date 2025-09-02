# 12.	Volume of a Cylinder: Find volume and cost (given milk cost per liter).
import math

def Calculate_Volume_and_Cost(Radius, Height,cost_per_litre):
    Volume_Cm3 = math.pi * Radius**2 * Height
    Volume_Litre = Volume_Cm3 / 1000 #convert cm3 to litre
    cost = Volume_Litre * cost_per_litre
    return Volume_Litre, cost
try:
    r = float(input("Enter radius in cm: "))
    h = float(input("Enter Height in cm: "))
    cost_per_litre = float(input("Enter Cost in ₹: "))

    volume, Total_cost = Calculate_Volume_and_Cost(r, h, cost_per_litre)
    print(f"\nVolume of Cylinder = {volume:.2f} liters")
    print(f"Total Cost of Milk = ₹{Total_cost:.2f}")
except ValueError:
  print("Please enter valid numeric values.")
