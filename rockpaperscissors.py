# Rock Paper Scissors game with Random library

import random 

# global variable that randomizes a choice everytime the code is ran
computer_choice = random.choice(['rock', 'paper', 'scissors'])

# global variable that sets the user choice
user_choice = input('Do you want rock, paper, or scissors?') 

print('Computer choice: ', computer_choice)


# loop function that checks the user input and determines if it matches/trumps the computer_choice value
if computer_choice == user_choice: 
    print('TIE') 
elif user_choice == 'rock' and computer_choice == 'scissors': 
    print('WIN') 
elif user_choice == 'paper' and computer_choice == 'rock': 
    print('WIN') 
elif user_choice == 'scissors' and computer_choice == 'paper': 
    print('WIN') 
else: 
    print('You lose, computer wins :)')