def convert(fraction):
    """
    Convert a fraction in X/Y format to a percentage rounded to the nearest int between 0 and 100, inclusive.

    Args:
        fraction (str): The fraction in X/Y format.

    Returns:
        int: The percentage, rounded to the nearest int between 0 and 100, inclusive.

    Raises:
        ValueError: If X and/or Y is not an integer, or if X is greater than Y.
        ZeroDivisionError: If Y is 0.
    """

    num, den = map(int, fraction.split('/'))
    if den == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")
    if num > den:
        raise ValueError("The numerator cannot be greater than the denominator.")
    return round(num / den * 100)


def gauge(percentage):
    """
    Return a str that is:
        "E" if that int is less than or equal to 1,
        "F" if that int is greater than or equal to 99,
        and "Z%" otherwise, wherein Z is that same int.

    Args:
        percentage (int): The percentage.

    Returns:
        str: The str representation of the percentage.
    """

    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


def main():
    """
    The main function.
    """

    while True:
        try:
            fraction = input("Enter the fuel tank's fraction (e.g. X/Y): ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except ValueError:
            print("Invalid fraction format. Please try again.")
        except ZeroDivisionError:
            print("Denominator cannot be zero. Please try again.")


if __name__ == "__main__":
    main()
