'''
How to Test
To test your tests, run pytest test_bank.py. Be sure you have a copy of a bank.py file in the same folder. Try to use correct and incorrect versions of bank.py to determine how well your tests spot errors:

Ensure you have a correct version of bank.py. Run your tests by executing pytest test_bank.py. pytest should show that all of your tests have passed.
Modify the correct version of bank.py, changing the values provided for each greeting. Your program might, for example, mistakenly provide $100 to a customer greeted by “Hello” and $0 to a customer greeted with “What’s up”! Now, run your tests by executing pytest test_bank.py. pytest should show that at least one of your tests has failed.
'''

from bank import value


def test_greeting():
    assert value("hello world") == 0
    assert value("HELLO WORLD") == 0
    assert value("hi world") == 20
    assert value("HI WORLD") == 20
    assert value("wassup world") == 100
    assert value("WASSUP WORLD") == 100