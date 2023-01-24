#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Area of a square
    args: size - of integer value"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """ Area of a square
    args: size - of integer value"""
    def area(self):
        area = self.__size
        return area * area
