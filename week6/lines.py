"""
Even so, in a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of
a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not 
specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist,
the program should instead exit via sys.exit.
Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring should not be considered a 
comment.) Assume that any line that only contains whitespace is blank.
Hints
Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods, including lstrip and startswith.
Note that open can raise a FileNotFoundError, per docs.python.org/3/library/exceptions.html#FileNotFoundError.
You might find it helpful to test your program on, e.g., some of Week 6’s source code as well as on programs of your own.
"""

import sys

# Write your code here
if len(sys.argv) != 2:
    sys.exit()

# Write your code here 
if sys.argv[1].endswith(".py") == False:
    sys.exit()

# Write your code here
try:
    file = open(sys.argv[1])
    count = 0
    for line in file:
        if line.startswith("#") or line.strip() == "":
            continue
        count += 1
        print(count)
        
except FileNotFoundError:
    sys.exit()


