# 57.	Reverse Words in String: e.g., "Hello how are you" → "you are how Hello"

def reverseWord(s):
    words = s.split()
    reverseWord = words[::-1]
    return ' '.join(reverseWord)

s = "Hello how are you"
print(reverseWord(s))
