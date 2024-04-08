# Number Guessing Game: Build a simple game where the computer generates a random number, 

# and the user has to guess it. Provide hints like “too high” or “too low” to guide the user.

import random

computer_number = random.randint(0, 101)
while True:
    user_guess = int(input("Guess a number between 0 and 100: "))
    if computer_number == user_guess:
        print("You got it!")
        break
    elif computer_number < user_guess:
        print("Too high!")
    elif computer_number > user_guess:
        print("Too low!")
