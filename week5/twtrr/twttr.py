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
# Updated twttr.py
def main():
    text = input("Input: ")
    output = shorten(text)
    print(f"Output: {output}")


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    shortened = []
    for c in word:
        if c.casefold() not in vowels:
            shortened.append(c)
    output = str("".join(shortened))
    return output


if __name__ == "__main__":
    main()