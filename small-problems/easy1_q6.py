# Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum 
# or the product of all numbers between 1 and the entered integer, inclusive.
#====================================================================================
# Example 1:
# Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s
# 
# The sum of the integers between 1 and 5 is 15.
# ===================================================================================
# Example 2: 
# Please enter an integer greater than 0: 6
# Enter "s" to compute the sum, or "p" to compute the product. p

# The product of the integers between 1 and 6 is 720.
#=====================================================================================

# Function to calculate the sum
def sum_of_numbers(number):
    return sum(range(1, number+1))

# Function to calculate the product
def product_of_numbers(number):
    product = 1
    for num in range(1, number+1):
        product *= num
    return product

while True:
    # Prompt to enter an integer
    prompt1 = "Please enter an integer greater than 0:"

    # Prompt to enter "s" or "p"
    prompt2 = """Please enter the string "s" or "p" """
    # Variable that holds the prompt for an integer. 
    num = int(input(prompt1))
            
    # Variable that holds the prompt of operations.
    operation = input(prompt2)
    print()

    # Conditionals to determine the correct operations.
    if operation == "s":
        print(f"The sum of {num} is {sum_of_numbers(num)}")
    elif operation == "p":
        print(f"The product of {num} is {product_of_numbers(num)}")
    else:
        print("That is an invalid operation.")
    
    response = input("Perform another calculation? (y/n):")
    while response not in ['y', 'n']:
        print("Invalid! Please select on 'y' or 'n'. ")
        response = input()
    
    if response == 'n':
        break


'''
# User Input
number = int(input('Please enter an integer greater than 0: '))
print(f'You entered {number}\n')

choice = input("""Enter "s" to compute the sum, or "p" to compute the product: """)
print(f'You entered {choice}')

# Calculations
sum_ = sum(range(number, +1))
print(f"The sum is {sum_}")

product = 1 
for num in range(number):
    product *= num
print(f"The product is {product}")
'''


    





