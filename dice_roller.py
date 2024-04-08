import random
#dice number of sides
dice_sides = int(input("how sides does your dice have ?\n"))

# Roll the dice
dice_roll = random.randint(1, dice_sides)

# Print the result
print(f"You rolled a {dice_roll}.")