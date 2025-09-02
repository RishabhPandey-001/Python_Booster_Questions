def swap_min_max(d):
    if not d:  # if dictionary is empty
        return d
    
    # Find keys for min and max values
    min_key = min(d, key=d.get)
    max_key = max(d, key=d.get)
    
    # Swap their values
    d[min_key], d[max_key] = d[max_key], d[min_key]
    return d


# Example usage
data = {"a": 10, "b": 3, "c": 25, "d": 7}
print("Original Dictionary:", data)

swapped = swap_min_max(data)
print("After Swapping Min & Max Values:", swapped)
