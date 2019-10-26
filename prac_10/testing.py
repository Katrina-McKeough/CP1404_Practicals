"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    # assert test with custom message,
    # used to see if Car sets the fuel correctly (default and passed in)
    # this should pass (no output)
    assert test_car.fuel == 0, "Car does not set default fuel correctly"
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not set passed in fuel correctly"


def format_phrase_as_sentence(phrase=''):
    """
    Format a phrase as a sentence, starting with a capital and ending with a single full stop. 
    >>> format_phrase('hello')
    'Hello.'
    >>> format_phrase('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_phrase('i need to watch V for Vendetta.')
    'I need to watch V for Vendetta.'
    """

    sentence = ""
    for i, letter in enumerate(phrase):
        if i == 0:
            letter = letter.capitalize()
        sentence += letter
    if not sentence[-1] == ".":
        sentence += "."
    return sentence


run_tests()

doctest.testmod()
