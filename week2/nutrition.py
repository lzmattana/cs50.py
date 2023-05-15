"""implement a program that prompts consumers users to input a fruit (case-insensitively) 
and then outputs the number of calories in one portion of that fruit, 
TESTCASE:
Run your program with python nutrition.py. Type Apple and press Enter. Your program should output:
Calories: 130   
Run your program with python nutrition.py. Type Avocado and press Enter. Your program should output:
Calories: 50
Run your program with python nutrition.py. Type Sweet Cherries and press Enter. Your program should output
Calories: 100
Run your program with python nutrition.py. Type Tomato and press Enter. Your program should output nothing.
"""
fruits = [
    {'name': 'Apple', 'calories': '130'},
    {'name': 'Avocado', 'calories': '50'},
    {'name': 'Banana', 'calories': '90'},
    {'name': 'Sweet Cherries', 'calories': '100'},
    {'name': 'Kiwifruit', 'calories': '90'},
    {'name': 'Pear', 'calories': '100'},
]

fruit = input("Please enter a fruit: ").lower()

for f in fruits:
    if fruit == f['name'].lower():
        print("Calories:", f['calories'])
        break