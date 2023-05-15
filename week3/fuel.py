"""
Fuel gauges indicate, often with fractions, just how much fuel is in a tank. 
For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.
In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer,
and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.
If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.)
Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""
while True:
    try:
        fraction = input("Enter the fuel tank's fraction (e.g. X/Y): ")
        num, den = map(int, fraction.split('/'))
        if den == 0:
            print("Denominator cannot be zero. Please try again.")
            continue
        if num > den:
            print("The numerator cannot be greater than the denominator. Please try again.")
            continue
        percentage = num / den * 100
        if percentage <= 1:
            print("E")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{round(percentage)}%")
        break
    except ValueError:
        print("Invalid fraction format. Please try again.")
    except ZeroDivisionError:
        print("Denominator cannot be zero. Please try again.")
