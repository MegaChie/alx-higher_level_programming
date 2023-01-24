#!/usr/bin/python3
""" square """


class Square:
    """ Create a Square
    args: size - integer value grater or equal to 0 """
    def __init__(self, size=0):
        self.__size = size

    """ Create a Square """
    def size(self):
        return self.__size

    """ Create a Square
    args: value - integer value grater or equal to 0 """
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    """ Create a Square """
    def area(self):
        return self.__size * self.__size

    """ Create a Square
    args: other - integer value grater or equal to 0 """
    def __le__(self, other):
        return self.area() <= other.area()

    """ Create a Square
    args: other - integer value grater or equal to 0 """
    def __lt__(self, other):
        return self.area() < other.area()

    """ Create a Square
    args: other - integer value grater or equal to 0 """
    def __ge__(self, other):
        return self.area() >= other.area()

    """ Create a Square
    args: other - integer value grater or equal to 0 """
    def __ne__(self, other):
        return self.area() != other.area()

    """ Create a Square
    args: other - integer value grater or equal to 0 """
    def __gt__(self, other):
        return self.area() > other.area()

    """ Create a Square
    args: other - integer value grater or equal to 0 """
    def __eq__(self, other):
        return self.area() == other.area()
