# This function will be re-used in various parts of the code
def prompt(message):
    print(f"--> {message}")

# Catching `Value/Error` exception when the argument can't be converted into an integer.
def invalid_number(num_str):
    try:
        int(num_str)
    except ValueError:
        return True
    
    return False

# Calling the function in line 2 to welcome the user to the program. 
prompt('Welcome to Calculator')

# Calling the function in line 2 and prompting the user to enter the first integer.
prompt("What's the first number?")
number1 = input()

# While loop checking if the first input is valid if not, it  Calls the function in line 6 informing the
# user that the input in invalid. Loop terminates when input is valid.
while invalid_number(number1):
    prompt(f'{number1} is not a valid number, please enter a valid number.')
    number1 = input()

# Prompting the user for the second integer
prompt("What's the second number?")
number2 = input()

# While loop checking if the second input is valid if not, it  Calls the function in line 6 informing the
# user that the input in invalid. Loop terminates when input is valid.

while invalid_number(number2):
    prompt(f'{number2} is not a valid number, please enter a valid number.')

# Ask the user which operation they would like to perform by typing 1,2,3 or 4.
prompt("Type the number for the operation you want to perform?\n1.Add\n2.Subtract\n3.Multiply\n4.Divide")
operation = input()

# A while loop that checks if the valid operation input choice was selected.
while operation not in ["1", "2", "3", "4"]:
    prompt('You must choose 1, 2, 4, or 4')
    operation = input()

# Using a match/case statement to work through the logic of the calculations for each operation:
match operation:
    case "1":
        output = int(number1) + int(number2)
    case "2":
        output = int(number1) - int(number2)
    case "3":
        output = int(number1) * int(number2)
    case "4":
        output = int(number1) / int(number2)

prompt(f"The result is: {output}")