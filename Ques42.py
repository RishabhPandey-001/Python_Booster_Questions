# 42.	Number Pyramid:
# 1
# 1 2 1
# 1 2 3 2 1

rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    for j in range(i - 1, 0, -1):
        print(j, end=' ')
    print()  


