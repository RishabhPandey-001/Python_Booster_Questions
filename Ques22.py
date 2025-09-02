# 22.	Dogs & Chickens Problem: Given total heads and legs, find the number of dogs and chickens.

def solve_dogs_chickens(heads, legs):
    for chickens in range(heads + 1):  
        dogs = heads - chickens      #Total heads = chickens + dogs -->>👉 c + d = 10
        if 2 * chickens + 4 * dogs == legs:  #Total legs = 2 legs per chicken + 4 legs per dog-->>👉 2c + 4d = 28
            return chickens, dogs
    return None, None


heads = int(input("Enter the number of heads: "))
legs = int(input("Enter the number of legs: "))

chickens, dogs = solve_dogs_chickens(heads, legs)

if chickens is not None:
    print(f"Chickens: {chickens}, Dogs: {dogs}")
else:
    print("No solution found.")
