# 55.	Search in List: Check if a number exists in a list.
def check_num(lst, target):
    for i in lst:
        if i == target:
            return True
    return False

Elements = [1,4,56,3,5,9,7]
target = int(input("Enter the number to search: "))
if check_num(Elements, target):
    print("Number found in the list.")
else:
    print("Number not found in the list.")
        