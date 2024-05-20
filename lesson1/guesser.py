# This program is a game - guess the number, higher or lower.
# What happens when you guess something that isn't a number?
# Can we count the number of guesses the person makes and print that when they win?

# Skills:
# - Printing to terminal
# - Getting user input
# - Converting a string to a number
# - While loops
# - If/elif/else statements
# - String interpolation

import random

numberToGuess = random.randint(0, 100)
guess = None

print("Welcome to my number guessing game! Guess a number from 1-100")

while guess != numberToGuess:
    guess = int(input("Guess: "))
    if guess < numberToGuess:
        print(f"Nope, {guess} is lower than the number I'm thinking of.")
    elif guess > numberToGuess:
        print(f"Nope, {guess} is higher than the number I'm thinking of.")
    else:
        print(f"You got it! I was thinking of {guess}.")
