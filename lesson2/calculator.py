# When writing a program, first write some pseudocode before writing any code:

# Ask the user for the first number
# Ask the user for the second number
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal

# 01/22/2025 Refactoring parts of the program

# Welcome the user to the program: 
#print(" Welcome to the Calculator!")

# Ask the user for the first number
# print(" What's the first number?")
def prompt(message):
    print(f"==> {message}")

# 01/22/2025: The invalid_number function
def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True
    
    return False

prompt('Welcome to Calculator!')


prompt("What's the first number?")
number1 = input()

# 01/ 22/2024: Adding looping logic to check whether input is valid
while invalid_number(number1):
    prompt("Hmm... that doesn't look like a valid number.")
    number1 = input()


prompt("What's the second number?")
number2 = input()

# 01/ 22/2024: Adding looping logic to check whether input is valid
while invalid_number(number2):
    prompt("Hmm... that doesn't look like a valid number.")
    number2 = input()

# number1 = input()
# print("=> What's the second number?")
# number2 = input()

# printing the numbers
# print(f'{number1} {number2')

print("""What operation would you like to perform?
      (1)Add (2)Subtract (3)Multiply (4)Divide""")
operation = input()
# 01/ 22/2024: Adding looping logic to validate the operation requested 
# by the user. The only
# valid inputs for the operation are '1','2','3','4'.
while operation not in ['1', '2', '3', '4']:
    prompt('You must choose 1, 2, 3 or 4')
    operation = input()


# perform if/else statement to perform arithmetic operations 
# based on user request.

# 01/22/2025 Replacing if/else with match case statement
# if operation == '1': # '1' represents addition
    # output = int(number1) + int(number2)
# elif operation == '2': # '2' represents subtraction
    # output = int(number1) - int(number2)
# elif operation == '3': # '3' represents multiplication
    # output = int(number1) * int(number2)
# elif operation == '4': # '4' represents multiplication
    # output = int(number1) / int(number2)

match operation:
    case '1':
        output = int(number1) + int(number2)
    case '2':
        output = int(number1) - int(number2)
    case '3': 
        output = int(number1) * int(number2)
    case '4':
        output = int(number1) / int(number2)

print(f"The result is: {output}")