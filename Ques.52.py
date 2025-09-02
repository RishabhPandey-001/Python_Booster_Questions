# 52.	Title Case Conversion: Convert string to title case without title().
def do_title_case(s):
    words = s.split()
    title_cased = []

    for word in words:
        if len(word) >0:
            title_cased.append(word[0].upper() + word[1:].lower())
        else:
            title_cased.append(word)
    return ' '.join(title_cased)
text = input("Enter the string: ")
converted = do_title_case(text)
print("Title case: ",converted)            