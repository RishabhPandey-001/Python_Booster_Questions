# 60.	Split List into Odds & Evens: Create two lists.
def Split_even_odds(lst):
    evens = []
    odds = []
    for i in lst:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    return evens, odds

lst = [1,5,2,4,6,3,8,7,9]
evens, odds = Split_even_odds(lst)

print("Evens: ",evens)
print("Odds: ", odds)