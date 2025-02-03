# 3. What will the following code output?

str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)

# My Prediction:

# This would output "hello there". This is because str2 was referencing to str1 in 
# line 4, however in line 5 str2 is now referencing the string "goodbye!"
# str1 is still referencing to the original string.

# Actual:
# Output: 'hello there'

# In Python, assignment of one variable's value to another variable makes both variables point to the 
# same object. Thus, after running line 4, both str1 and str2 reference the same string object. 
# However, that connection between the variables is broken if you assign a different object to 
# one of the variables. Thus, line 3 breaks the connection between str1 and str2. As a result, 
# str2 now references "goodbye!" while str1 continues to reference "hello there".

