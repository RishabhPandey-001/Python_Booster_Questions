# 43.	Floyd's Triangle:
# 1
# 2 3
# 4 5 6
# ...  

rows = int(input("Enter number of rows: "))
nums = 1
for i in range(1, rows +1):
    for j in range(1, i+1):
        print(nums, end = ' ')
        nums +=1 
    print()
