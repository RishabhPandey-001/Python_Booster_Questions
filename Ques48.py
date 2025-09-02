# 48.	Count Vowels: Count vowels in a string.
text = input("Enter string: ")
vowel = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowel:
        count += 1
print("number of vowels: ", count)        