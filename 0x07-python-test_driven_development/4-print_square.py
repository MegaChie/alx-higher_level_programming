#!/usr/bin/python3
""" prints a square shape.  """


def print_square(size):
    """ prints a square of hashtags.
    checks if input is integer and is bigger than 0
    if input is 0 it prints nothing  """
    text1 = "size must be an integer"
    text2 = "size must be >= 0"
    text3 = "size must be an integer"
    if type(size) is not int:
        raise TypeError(text1)
    if size < 0:
        raise ValueError(text2)
    if size < 0 and type(size) is float:
        raise TypeError(text3)
    if size == 0:
        return None
    for printer in range(size):
        print('#' * size)
