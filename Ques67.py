# 67.	Matrix Shape: Print rows and columns.

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

rows = len(matrix)
columns = len(matrix[0]) if matrix else 0
print("Rows: ", rows)
print("Columns: ", columns)