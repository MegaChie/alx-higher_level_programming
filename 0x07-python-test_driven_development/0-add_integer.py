##!/usr/bin/python3
"""  calculates the sum of two numbers """


def add_integer(a, b=98):
    """  add two numbers up.
    checks if input is numbers, and if given floats it converts to integers """
    if type(a) is float or type(b) is float:
        a = int(a)
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
