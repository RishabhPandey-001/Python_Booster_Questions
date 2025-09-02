# 53.	Max Item Without max(): Find the maximum in a list.
def Max_in_list(lst):
    if not lst:
        return None 

    max_val = lst[0]
    for item in lst:
        if item > max_val:
            max_val = item
    return max_val       
numbers = [3,4,5,8,9,7,6,12,4]
maximum = Max_in_list(numbers)
print("The max number in list is: ", maximum)