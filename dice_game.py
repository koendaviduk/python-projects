import random


# gets random int between 1 and 6 twice and returns the added value
def roll_dice():
    dice_total = random.randint(1, 6) + random.randint(1, 6)
    return dice_total
# asks players for names

player1 = input("Enter player 1's name:\n")
player2 = input("Enter player 2's name:\n")

# gets the value from the random dice rolls and assigns accordingly
roll1 = roll_dice()
roll2 = roll_dice()

print(player1, 'rolled', roll1)
print(player2, 'rolled', roll2)

# math check
if roll1 > roll2:
    print(player1, 'wins!')
elif roll1 < roll2:
    print(player2, 'wins!')
else:
    print('Tie!')