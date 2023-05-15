"""
TESTCASE:
Run your program with python plates.py. Type CS50 and press Enter. Your program should output:
Valid
Run your program with python plates.py. Type CS05 and press Enter. Your program should output:
Invalid
Run your program with python plates.py. Type CS50P and press Enter. Your program should output
Invalid
Run your program with python plates.py. Type PI3.14 and press Enter. Your program should output
Invalid
Run your program with python plates.py. Type H and press Enter. Your program should output
Invalid
Run your program with python plates.py. Type OUTATIME and press Enter. Your program should output
Invalid
"""
import re  # Importing the regular expression module

def is_valid(s):  # Defining a function that takes a string as input
    if not re.match(r'^[A-Z]{2}[A-Z0-9]{0,3}[A-Z0-9]{1}$', s):
        # Checking if the input string matches the pattern defined by the regular expression
        # The pattern requires two uppercase letters, followed by up to three uppercase letters or digits,
        # and ending with exactly one uppercase letter or digit
        return False  # If the input string doesn't match the pattern, return False
    
    if re.search(r'\d[A-Z]\d', s):
        # Checking if the input string contains a digit, followed by an uppercase letter, followed by a digit
        # If so, the vanity plate is not valid
        return False  # If the input string contains a digit, followed by an uppercase letter, followed by a digit, return False
    
    if s[2].isdigit() and s[2] == '0':
        # Checking if the third character in the input string is a digit and is equal to '0'
        # If so, the vanity plate is not valid
        return False  # If the third character in the input string is a digit and is equal to '0', return False
    
    return True  # If none of the above conditions are met, the vanity plate is valid

# Asking the user to enter a vanity plate
plate = input("Enter a vanity plate: ")

if is_valid(plate):  # Checking if the entered vanity plate is valid by calling the is_valid function
    print("Valid")  # If the entered vanity plate is valid, print "Valid"
else:
    print("Invalid")  # If the entered vanity plate is not valid, print "Invalid"
