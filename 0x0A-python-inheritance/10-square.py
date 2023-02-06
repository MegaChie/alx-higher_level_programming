#!/usr/bin/python3
""" user defined class. """
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """ Square #1. """
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    """ Square #1. """
    def area(self):
        return self.__size * self.__size
