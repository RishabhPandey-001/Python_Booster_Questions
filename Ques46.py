# 46.	Character Frequency: Count occurrences of a character in a string.
st = str(input("Enter the string: "))
frequency = {}
for char in st:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print("Character Frequencies:")
for char, count in frequency.items():
    print(f"'{char}': {count}")
