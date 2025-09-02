# 71.	Most Frequent Word in Song: Find the most repeated word.

def most_frequent_word(text):
    # Convert to lowercase and split into words
    words = text.lower().split()
    
    # Dictionary to count word frequencies
    freq = {}
    for word in words:
        word = word.strip(".,!?;:")  # remove punctuation
        freq[word] = freq.get(word, 0) + 1
    
    # Find the word with maximum frequency
    max_word = max(freq, key=freq.get)
    return max_word, freq[max_word]


song = """
Twinkle twinkle little star
How I wonder what you are
Up above the world so high
Like a diamond in the sky
Twinkle twinkle little star
How I wonder what you are
"""

word, count = most_frequent_word(song)
print(f"Most frequent word: '{word}' (appears {count} times)")
