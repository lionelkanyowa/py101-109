# 2. How can you determine whether a given string ends with an exclamation mark (!)? Write some 
# code that prints True or False depending on whether the string ends with an exclamation mark.

str1 = "come over here!" # True
str2 = "What's up, Doc?" # False

# print('!' in str1)
# print('!' in str2)

print(str1.endswith('!'))
print(str2.endswith('!'))