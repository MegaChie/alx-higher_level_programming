#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Access and update private attribute
    args: size - of integer value and is bigger or equal to 0"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """ Access and update private attribute """
    def area(self):
        area = self.__size
        return area ** 2

    """ Access and update private attribute """
    def size(self):
        return self.__size

    """ Access and update private attribute
    args: value - of integer value and is bigger or equal to 0"""
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
