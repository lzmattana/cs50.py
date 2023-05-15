"""
{
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items,
one per line, until the user inputs control-d (which is a common way of ending one’s input to a program).
After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($)
and formatted to two decimal places. Treat the user’s input case insensitively.
Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.
"""
# Define the menu
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Initialize the total cost to zero
total_cost = 0

# Prompt the user for inputs until EOF is reached
try:
    while True:
        # Display the prompt
        print("Please enter an item (or press ctrl-d to finish): ")

        # Get the user's input and convert it to title case
        item = input().strip().title()

        # Check if the item is on the menu
        if item in menu:
            # Update the total cost
            total_cost += menu[item]

            # Display the total cost with two decimal places
            print(f"Total cost so far: ${total_cost:.2f}\n")
        else:
            # Display an error message if the item is not on the menu
            print("Sorry, that item is not on the menu. Please try again.\n")

# Catch the EOFError when the user inputs ctrl-d
except EOFError:
    # Display the final total cost
    print(f"Your total is ${total_cost:.2f}. Thanks for your order!")
