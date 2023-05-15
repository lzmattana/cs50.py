"""
implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase.
Run your program with python twttr.py. Type Twitter and press Enter. Your program should output:
Twttr
Run your program with python twttr.py. Type What's your name? and press Enter. Your program should output:
Wht's yr nm?
Run your program with python twttr.py. Type CS50 and press Enter. Your program should output
CS50
"""
text = input("Please enter some text: ")

# Create an empty string to store the text with vowels removed
no_vowels_text = ""

# Iterate over each character in the input string
for c in text:
    # If the character is not a vowel, add it to the no_vowels_text string
    if c.lower() not in ['a', 'e', 'i', 'o', 'u']:
        no_vowels_text += c

print(no_vowels_text)
