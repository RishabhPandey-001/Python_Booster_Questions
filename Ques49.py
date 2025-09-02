# 49.	Remove a Character: Delete a specific character from a string.
text = input("Enter the string: ")
char_to_remove = input("enter the string to remove: ")
new_string = text.replace(char_to_remove, "")
print("string after removing the character: ", new_string)
6