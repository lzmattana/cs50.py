"""
TESTCASE:
Run your program with python deep.py. Type 42 and press Enter. Your program should output:
Yes
Run your program with python deep.py. Type Forty Two and press Enter. Your program should output:
Yes
Run your program with python deep.py. Type forty-two and press Enter. Your program should output
Yes
Run your program with python deep.py. Type 50 and press Enter. Your program should output
No
"""


text = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

#uso de strip para checar espaços
if text.strip() == "42" or text.lower() == "forty two" or text == "forty-two":
    print("Yes")
else:
    print("No")