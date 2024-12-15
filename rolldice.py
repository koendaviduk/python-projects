# simple roll dice program 

import random

# sets a global value that rolls a random # everytime the program is run
roll = random.randint(1, 6)

# global variable gathering the user guess/input
guess = int(input('Guess the dice roll:\n'))

# main loop function checking if the user input matches the random # generated via roll variable
if guess == roll:
    print('Correct! They rolled a ' + str(roll))
else:
    print('Wrong! They rolled a ' + str(roll))