# 51.	Remove Duplicates from List: Create a list with unique elements.
def remove_duplicate(lst):
    return list(set(lst))

original_list = [1,1,2,2,2,3,4,5,5]
unique_list = remove_duplicate(original_list)
print("The Unique Elements of list are:", unique_list)