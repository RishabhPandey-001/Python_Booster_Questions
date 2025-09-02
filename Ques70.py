# 70.	Sort List Without Built-ins: Implement sorting manually.
def bubble_sort(arr):
    n = len(arr)
    for i in range (n):
        for j in range (0, n-i-1):
            if arr[j]> arr[j+1]:
                #swap
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original List:", numbers)
print("Sorted List:", bubble_sort(numbers))



# Selection Sort Implementation
# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         # Swap
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr


# # Example
# numbers = [29, 10, 14, 37, 13]
# print("Original List:", numbers)
# print("Sorted List:", selection_sort(numbers))
