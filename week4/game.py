'''
I’m thinking of a number between 1 and 100…

What is it?
In a file called game.py, implement a program that:

Prompts the user for a level,
. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and
, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
Hints
Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html.

'''

# Import the 'random' module to generate random numbers.
import random

# Start an indefinite loop to keep the game running until the user decides to exit.
while True:
    try:
        # Prompt the user to enter a 'level' (an integer).
        level = int(input('Level: '))

        # Generate a random number 'x' between 1 and the user-provided 'level'.
        x = random.randint(1, level)

        # Start another indefinite loop for the guessing game.
        while True:
            # Prompt the user to make a 'guess' (an integer).
            guess = int(input("Guess: "))

            # Compare the user's guess to the random number 'x'.
            if guess > x:
                print("Too large!")
            elif guess < x:
                print("Too small!")
            elif guess == x:
                print("Just right!")

                # Raise an 'EOFError' to exit the inner loop and end the game.
                raise EOFError

    # Handle a 'ValueError' if the user enters a non-integer value for 'level' or 'guess'.
    except ValueError:
        pass

    # Handle an 'EOFError' if the user correctly guesses the number and chooses to exit the game.
    except EOFError:
        break

# The program continues until the user decides to exit by correctly guessing the number and raising an 'EOFError'.
