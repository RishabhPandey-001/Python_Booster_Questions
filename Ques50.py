# 50.	Palindrome Check: Check if a string is a palindrome.
def isPalindrome(s):
 s = ''.join(char.lower() for char in s if char.isalnum())
 return s == s[::-1]

text = input("Enter the string: ")
if isPalindrome(text):
 print("This string is Palindrome")

else:
 print("This is not a Palindrome")
