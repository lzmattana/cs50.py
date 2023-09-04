'''
In The Sound of Music, there’s a song sung largely in English, So Long, Farewell, with these lyrics, wherein “adieu” means “goodbye” in French:

Adieu, adieu, to yieu and yieu and yieu

Of course, the line isn’t grammatically correct, since it would typically be written (with an Oxford comma) as:

Adieu, adieu, to yieu, yieu, and yieu

To be fair, “yieu” isn’t even a word; it just rhymes with “you”!

In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and
 names with
 commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

Hints
Note that the inflect module comes with quite a few methods, per pypi.org/project/inflect. You can install it with:
pip install inflect
'''

# Import the 'inflect' library, which is used for pluralization and other linguistic operations.
import inflect

# Create an instance of the 'inflect' engine and store it in the variable 'p'.
p = inflect.engine()

# Initialize an empty list called 'name_list' to store user-entered names.
name_list = []

while True:
    try:
        # Prompt the user for input, strip leading/trailing whitespace, and capitalize the name.
        name = input("Name: ").strip().title()
        # Append the formatted name to the 'name_list'.
        name_list.append(name)
    except EOFError:
        # If an EOFError is raised (typically when using Ctrl+D or Ctrl+Z to exit input),
        # print a farewell message and the joined list of names using the 'inflect' engine.
        print()
        print("Adieu, adieu, to", p.join(name_list))
        break