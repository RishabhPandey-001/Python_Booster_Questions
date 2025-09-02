# 45.	Extract Username from Email: e.g., nitish24singh@gmail.com → nitish24singh.
email = input("Enter the Email: ")
username = ""
for char in email:
    if char =='@':
        break
    username += char
print("The username is: ", username)    