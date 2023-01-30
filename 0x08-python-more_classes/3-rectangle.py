#!/usr/bin/python3
""" More Classes and Objects  """


class Rectangle:
    """  String representation. """
    @property
    def width(self):
        return self.__width

    """ String representation.
    args: value - of integer  type """
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ String representation. """
    @property
    def height(self):
        return self.__height

    """ String representation. """
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ String representation.
    Args: width - of integer type
          height - of integer type """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """ String representation. """
    def area(self):
        return self.__height * self.__width

    """ String representation. """
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    """ String representation. """
    def __str__(self):
        printed = ""
        if self.__height == 0 or self.__width == 0:
            return printed
        for place in range(self.__height):
            if place == self.__height - 1:
                printed += ('#' * self.__width)
            else:
                printed += (('#' * self.__width) + '\n')
        return printed
