#!/usr/bin/python3
""" ByteCode -> Python #5 """


import math


class MagicClass:
    """ magic calculation
    args: radius - integer value that relates to circle dimensions """
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    """ magic calculation
    args: radius - integer value that relates to circle dimensions """
    def area(self):
        return self.__radius ** 2 * math.pi

    """ magic calculation
    args: radius - integer value that relates to circle dimensions """
    def circumference(self):
        return 2 * math.pi * self.__radius
