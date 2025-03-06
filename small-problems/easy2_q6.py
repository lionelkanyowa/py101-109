# q.6 Write a function that returns the next to last word in the string argument. 

# Words are any sequence on non-blank characters.

# You may assume that the input string will always contain at least two words.


def penultimate(string):
    words = string.split()
    return words[-2]


print(penultimate("last word") == "last")
print(penultimate("Launch School is great") == "is")