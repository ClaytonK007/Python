#
#   Create a guessing game. Allow user to guess a number between 1 and 100. Provide hints.
#   Import the random module to generate random integer.
#
import random

secret = random.randint(1, 100)
attempts = 0

while True:
    try:
        user_input = input("Guess a number between 1 and 100 or 'q' to quit: ")
        if user_input == "q":
            print(f"Game over. The number was {secret}.")
            break
        guess = int(user_input)
    except ValueError:
        ("Invalid input. Please enter a number.")
        continue
    
    attempts += 1

    if guess < secret:
        print("Too low. Guess again...")
    elif guess > secret:
        print("Too high. Guess again...")
    else:
        print(f"Congrats!!! You guessed the correct number in {attempts} attempts.")
        break

