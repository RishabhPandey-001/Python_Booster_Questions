# 30.	Unique Combinations of 1,2,3,4: Print all unique combinations

from itertools import permutations

numbers = [1,2,3,4]
print("All unique combinatins:")
for perm in permutations(numbers):
    print(perm)
