# 1. Will the code below raise an error?

numbers = [1, 2, 3]
numbers[6] = 5
print(numbers)

# Yes this will raise an error because the list only goes up to the second index
# and the variable is being re-initialized for the sixth index.