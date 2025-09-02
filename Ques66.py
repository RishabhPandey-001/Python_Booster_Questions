# 66.	Integer to String: Convert without str().
#1st method

# num = 123
# string_num = "%s" % num
# print(string_num)
# print(type(string_num))

#2nd method

# num = 123
# string_num = "{}".format(num)
# print(string_num)
# print(type(string_num))

#3rd method

num = 123
string_num = f"{num}"
print(string_num)
print(type(string_num))