"""
Here’s how to test your code manually:

Run your program with python meal.py. Type 7:00 and press Enter. Your program should output:
breakfast time   
Run your program with python meal.py. Type 7:30 and press Enter. Your program should output:
breakfast time
Run your program with python meal.py. Type 12:42 and press Enter. Your program should output
lunch time
Run your program with python meal.py. Type 18:32 and press Enter. Your program should output
dinner time
Run your program with python meal.py. Type 11:11 and press Enter. Your program should output nothing.
"""
# The convert function takes a time string in the format of "h:mm a.m." or "h:mm p.m." and converts it to a float representing the hour in 24-hour format.
def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    if "p.m." in time.lower() and hours != 12:
        hours += 12
    elif "a.m." in time.lower() and hours == 12:
        hours = 0
    return hours + minutes/60

# In the main function, the user is prompted to enter a time in either 24-hour or 12-hour format with AM/PM. Then,
# the convert function is used to convert the time string to a float representing the hour in 24-hour format.
def main():
    time = input("Enter the time (e.g. 7:30 a.m. or 19:30): ")
    hour = convert(time)

    if 7 <= hour < 12:
        print("Breakfast time")
    elif 12 <= hour < 15:
        print("Lunch time")
    elif 18 <= hour < 23.5:
        print("Dinner time")

if __name__ == "__main__":
    main()
