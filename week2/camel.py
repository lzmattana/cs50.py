"""
TESTCASE:
Run your program with python camel.py. Type name and press Enter. Your program should output:
name   
Run your program with python camel.py. Type firstName and press Enter. Your program should output:
first_name
Run your program with python camel.py. Type preferredFirstName and press Enter. Your program should output
preferred_first_name
"""

# Prompt the user for a variable name in camel case
var_name = input("Enter a name: ")

# Convert the variable name to snake case
snake_case = ''
for c in var_name:
    if c.isupper():
        snake_case += '_' + c.lower()
    else:
        snake_case += c

# Output the variable name in snake case
print(snake_case.lstrip('_'))
