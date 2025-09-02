# 58.	Count Words in String: Find the number of words.

def count_string(s):
    words =  s.split()
    return len(words)

s = "Hello how are you Rishabh"
print(count_string(s))