# 63.	2D to 1D List: Flatten a matrix.
matrix = [[1, 2, 3], [4, 5], [6, 7, 8]]
flattened = [item for sublist in matrix for item in sublist]
print(flattened)  
