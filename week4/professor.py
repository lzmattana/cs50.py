'''
One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten different math problems for David to solve. For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. If the toy were to display 4 + 1 = , David would (hopefully) answer with 5. If David were to answer incorrectly, the toy would display EEE. And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).
In a file called professor.py, implement a program that:
Prompts the user for a level, 
. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 
 digits. No need to support operations other than addition (+).
Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 10.
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:
import random
def main():
    ...
def get_level():
    ...
def generate_integer(level):
    ...
if __name__ == "__main__":
    main()
Hints
Note that you can raise an exception like ValueError with code like:
raise ValueError
Note that the random module comes with quite a few functions, per docs.python.org/3/library/random.html.

'''
import random

# Define the main function
def main():
    # Initialize equation count, score, and chances
    eqn = 10
    score = 0
    chances = 3

    # Get the level of difficulty from the user
    lvl = get_level()

    # Loop until all equations are answered
    while eqn != 0:
        # Check if the user has 3 chances to answer each equation
        if chances == 3:
            # Generate two random integers based on the level
            x, y = generate_integer(lvl)

        try:
            # Prompt the user to answer the equation
            user_answer = int(input(f"{x} + {y} = "))
            answer = x + y

            # Check if the user's answer is correct
            if user_answer == answer:
                eqn -= 1  # Reduce the remaining equation count
                score += 1  # Increase the score
                chances = 3  # Reset chances to generate a new equation
                continue
            else:
                raise ValueError  # Raise an error if the answer is incorrect

        except (ValueError, NameError):
            print("Invalid input. Try again.")
            chances -= 1  # Decrease the chances for incorrect input
            pass

        if chances == 0:
            print((f"{x} + {y} = {answer}"))  # Display the correct answer
            chances = 3  # Reset chances to generate a new equation
            eqn -= 1  # Reduce the remaining equation count
            continue

    # Display the final score
    print(f"Score: {score}")

# Function to get the level of difficulty from the user
def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 1 <= n <= 3:
                return n
        except:
            pass

# Function to generate random integers based on the level of difficulty
def generate_integer(level):
    level_ranges = {1: (0, 9), 2: (10, 99), 3: (100, 999)}
    
    if level in level_ranges:
        x_range, y_range = level_ranges[level]
        x = random.randint(x_range, y_range)  # Use the entire range as arguments
        y = random.randint(x_range, y_range)
        return x, y
    else:
        raise ValueError("Invalid level provided")


# Example usage:
# x, y = generate_integer(2)  # Generates random integers in the range (10, 99)

# Entry point of the program
if __name__ == "__main__":
    main()
