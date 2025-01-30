# This is to review the pseudocode chapter and attempt any challenges given.

# Take a look at the given pseudocode:

# START

# Given a collection of integers called "numbers"

# ET iterator = 1
# SET savedNumber = value within numbers collection at space 1

# WHILE iterator <= length of numbers
	# SET currentNumber = value within numbers collection at space "iterator"
	# IF currentNumber > savedNumber
		# savedNumber = currentNumber

	# iterator = iterator + 1

# PRINT savedNumber

def find_greatest(numbers):
    index = 0
    saved_number = numbers[index]
    
    while index < len(numbers):
        current_number = numbers[index]
        if current_number > saved_number:
            saved_number = current_number

        index += 1

    return saved_number


print(find_greatest([3, 4, 5, 6, 7, 2, 10]))