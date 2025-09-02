# 56.	Square List Elements: Create a new list with squares of old list items.
def new_square_list(lst):
    # def new_square_list(lst):
    # return [i ** 2 for i in lst]

    result = []
    for i in lst:
        result.append(i ** 2)
    return result
    
numbers = [2,3,4,5,6,7,8]    
squares = new_square_list(numbers)
print("The new Square list of elements is: ", squares)