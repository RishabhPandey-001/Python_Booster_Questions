# 62.	Replace Item in List: Modify list if item found.
Mylist = [1,2,3,4,5]
item_to_replace = 4
new_item = 45

if item_to_replace in Mylist:
    index = Mylist.index(item_to_replace)
    Mylist[index] = new_item
    
print(Mylist)    