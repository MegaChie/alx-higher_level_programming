#!/usr/bin/python3
""" More Classes and Objects """


class Rectangle:
    """ Eval is magic. """
    @property
    def width(self):
        return self.__width

    """ Eval is magic.
    args: value - of integer  type """
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ Eval is magic. """
    @property
    def height(self):
        return self.__height

    """ Eval is magic. """
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ Eval is magic.
    Args: width - of integer type
          height - of integer type """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """ Eval is magic. """
    def area(self):
        return self.__height * self.__width

    """ Eval is magic. """
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    """ Eval is magic. """
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

    """ Eval is magic. """
    def __repr__(self):
        first = str(self.__width)
        second = str(self.__height)
        result = "Rectangle(" + first + ", " + second + ")"
        return result
