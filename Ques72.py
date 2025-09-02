def list_to_dict(numbers):
    return {num: num ** 2 for num in numbers}


numbers = [1, 2, 3, 4, 5]
result = list_to_dict(numbers)

print("Original List:", numbers)
print("Dictionary (number: square):", result)
