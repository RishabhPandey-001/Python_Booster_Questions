# 59.	Check Ascending Order: Verify if a list is sorted.

def Ascen_order(lst):
    return lst == sorted(lst)

lst = ["apple", "banana", "cherry"]
print(Ascen_order(lst))