#!/usr/bin/python3
""" More Classes and Objects  """


class Rectangle:
    """  Real definition of a rectangle. """
    @property
    def width(self):
        return self.__width

    """ Real definition of a rectangle.
    args: value - of integer  type """
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ Real definition of a rectangle. """
    @property
    def height(self):
        return self.__height

    """ Real definition of a rectangle. """
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ Real definition of a rectangle.
    Args: width - of integer type
          height - of integer type """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """ Real definition of a rectangle. """
    def area(self):
        return self.__height * self.__width

    """ Real definition of a rectangle. """
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
