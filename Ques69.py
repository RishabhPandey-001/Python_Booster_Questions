# # matrix multiplication.

def matrix_multiply(A , B):
    if len(A[0]) != len(B):
        print("Matrix multiplication not possible! (Columns of A ≠ Rows of B)")
        return None
    
     # Resultant matrix of size (rows of A x columns of B)

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range (len(A)):
        for j in range (len(B[0])):
            for k in range (len(B)):
                result[i][j] += A[i][k] * B[k][j]

    return result

A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [7, 8],
    [9, 10],
    [11, 12]
]

print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

result = matrix_multiply(A, B)

print("\nResultant Matrix (A x B):")
for row in result:
    print(row)        

# import numpy as np

# # Define matrices as numpy arrays
# A = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])

# B = np.array([
#     [7, 8],
#     [9, 10],
#     [11, 12]
# ])

# # Multiply using numpy
# result = np.dot(A, B)   # or A @ B

# print("Matrix A:\n", A)
# print("\nMatrix B:\n", B)
# print("\nResultant Matrix (A x B):\n", result)
