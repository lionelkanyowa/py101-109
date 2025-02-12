import json
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

# Feature 2: Etracting messages in the program to a JSON File.

def messages(message, language='English'):
    return MESSAGE[language][message]


with open('calc_messages.json', 'r') as file:
    MESSAGE = json.load(file)


# Feature 1: Added a do/while loop to ask the user to perform another calculation.
while True:
        # Calling the function in line 2 to welcome the user to the program. 
    prompt(messages('Welcome'))
    prompt(messages('Welcome', 'Shona'))
    prompt(messages('Welcome', 'Bemba'))
    prompt(messages('Line Break'))
    


    # Calling the function in line 2 and prompting the user to enter the first integer.
    prompt(messages('First Number'))
    prompt(messages('First Number', 'Shona'))
    prompt(messages('First Number', 'Bemba'))
    

    
    number1 = input()
    prompt(f'{(messages('Chosen Output'))} {number1} (English)')
    prompt(f'{(messages('Chosen Output', 'Shona'))} {number1} (Shona)')
    prompt(f'{(messages('Chosen Output', 'Bemba'))} {number1} (Bemba)')
    prompt(messages('Line Break'))

    # While loop checking if the first input is valid if not, it  Calls the function in line 8 informing the
    # user that the input in invalid. Loop terminates when input is valid.
    while invalid_number(number1):
        prompt(f'{number1} {messages('First Invalid')}')
        prompt(f'{number1} {messages('First Invalid', 'Shona')}')
        prompt(f'{number1} {messages('First Invalid', 'Bemba')}')
        
        number1 = input()
        


    # Prompting the user for the second integer
    prompt(messages('Second Number'))
    prompt(messages('Second Number', 'Shona'))
    prompt(messages('Second Number', 'Bemba'))
    
    
    number2 = input()
    prompt(f'{(messages('Chosen Output'))} {number2}')
    prompt(f'{(messages('Chosen Output', 'Shona'))} {number2}')
    prompt(f'{(messages('Chosen Output', 'Bemba'))} {number2}')
    prompt(messages('Line Break'))

    # While loop checking if the second input is valid if not, it  Calls the function in line 6 informing the
    # user that the input in invalid. Loop terminates when input is valid.

    while invalid_number(number2):
        prompt(f'{number2} {messages('Second Invalid')}')
        prompt(f'{number2} {messages('Second Invalid', 'Shona')}')
        prompt(f'{number2} {messages('Second Invalid', 'Bemba')}')
        

        number2 = input()

    # Ask the user which operation they would like to perform by typing 1,2,3 or 4.
    prompt(messages('Select Operation'))
    prompt(messages('Select Operation', 'Shona'))
    prompt(messages('Select Operation', 'Bemba'))
    

    operation = input()

    # A while loop that checks if the valid operation input choice was selected.
    while operation not in ["1", "2", "3", "4"]:
        prompt(messages('Invalid Operation'))
        prompt(messages('Invalid Operation', 'Shona'))
        prompt(messages('Invalid Operation', 'Bemba'))
        

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

    prompt(f'{messages('Result')} {output} (English)')
    prompt(f'{messages('Result', 'Shona')} {output} (Shona)')
    prompt(f'{messages('Result', 'Bemba')} {output} (Bemba)')
    prompt(messages('Line Break'))
    


    # Feature 1: prompting the user if they want to perform another calculation 
    
    prompt((messages('Another Calculation')))
    prompt((messages('Another Calculation', 'Shona')))
    prompt((messages('Another Calculation', 'Bemba')))
    response = input()
    


    # Feature 1: A while loop that checks the correct input of strings 'y' and 'n'. If user enters anything 
    # other than the mentioned strings they are given a warning message and ask to enter those strings only.
    while response not in ['y', 'n']:
        prompt(messages('Invalid'))
        prompt(messages('Invalid', 'Shona'))
        prompt(messages('Invalid', 'Bemba'))
        
  
        response = input()
    # Feature 1: if the response of the user in 'n' then the do/while loop stops and user won't be asked to 
    # perform another calculation.
    if response == 'n':
        break
    
    #if response == 'n':
        #break
    #elif response not in ['y', 'n']:
        #prompt("Invalid input. Must be either 'y' or 'n'")
        #input()

