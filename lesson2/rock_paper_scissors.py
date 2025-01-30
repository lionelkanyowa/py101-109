# Rock_Paper_Scissors Walk-through
# A game played between two opponents. Both opponents choose an item from rock, paper, or scissors. The winner
# is decided according to the following rules.

# 1. If player a chooses rock and player b chooses scissors, player a wins.
# 2. if player a chooses paper and player b chooses rock, player a wins.
# 3. If player a chooses scissors and player b chooses paper, player  wins.
# 4. If both players choose the same item, neither wins. it's a tie.
# 
# This version of the game let's the user play against the computer. The game flow should go like this:
# 
# 1. User makes a choice.
# 2 The computer makes a choice
# 3. The winner is displayed.
#   

# Using a constant to make our code more readable so that it can be used anywhere in the program. This was
# implemented after the while loop in line 31. Originally it was 'while choice not in [rock, paper, scissors] 
import random

VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f'==> {message}')

# Code that asks the user to choose one of rock, paper or scissors.

# prompt('Choose one: rock, paper, scissors')
while True:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()
    
    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()
    # Allow program to make a choice for the computer
    computer_choice = random.choice(VALID_CHOICES)
    # Let the user know what the two choices are:

# Deciding the winner based on the conditions outlined at at the start. 
# We now write a conditional for the case where the user wins:
    prompt(f"You chose {choice}. \n==> Computer chose {computer_choice}")
    if ((choice == 'rock' and computer_choice == 'scissors') or
        (choice == 'paper' and computer_choice == 'rock') or 
        (choice == 'scissors' and computer_choice == 'paper')):
        prompt("*You win!*")
        # We now write a conditional for the case where the computer wins:
    elif ((choice == 'rock' and computer_choice == 'paper') or 
          (choice == 'paper' and computer_choice == 'scissors') or 
          (choice == 'scissors' and computer_choice == 'rock')):
        prompt('*Computer wins!*')
    else:
        prompt("It's a tie!")

    # Adding a conditional that allows the user to choose if the want to play another game:
    while True:
        prompt('Do you want to play again (y/n)?')
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        else:
            prompt("That's not a valid choice")
        
    if answer[0] == 'n':
        break

