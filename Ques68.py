# 68.	Matrix Multiplication Check: Verify if multiplication is possible.

def can_multiply(a, b):
    row_a , col_a = len(a), len(a[0])
    row_b, col_b = len(b), len(b[0])
    if col_a == row_b:
        return True, (col_a, row_b)
    else:
        return False, None

a = [[1,2,3],
     [4,5,6,]]

b = [[7,8]
     ,[5,6],
     [3,4]]   

possible , size = can_multiply(a,b)
if possible:
    print("✅ Multiplication is possible. Resultant matrix size:", size)
else:
    print("❌ Multiplication is NOT possible.")  