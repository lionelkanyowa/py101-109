# Write a function that returns a list that contains every other element of a list that is passed in as an argument. The values in the 
# returned list should be those values that are in the 1st, 3rd, 5th, and so on elements of the argument list.

def oddities(values):
    result = []
    for index in range(len(values)):
        if index % 2 == 0:
            result.append(values[index])
    return result
    # return values[::2]

    
print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])
print(oddities([1, 2, 3, 4]) == [1, 3])        
print(oddities(["abc", "def"]) == ['abc'])     
print(oddities([123]) == [123])                
print(oddities([]) == [])                      