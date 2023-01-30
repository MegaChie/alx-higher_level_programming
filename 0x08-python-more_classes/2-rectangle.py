#!/usr/bin/python3
""" More Classes and Objects  """


class Rectangle:
    """  Area and Perimeter. """
    @property
    def width(self):
        return self.__width

    """ Area and Perimeter.
    args: value - of integer  type """
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ Area and Perimeter. """
    @property
    def height(self):
        return self.__height

    """ Area and Perimeter. """
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ Area and Perimeter.
    Args: width - of integer type
          height - of integer type """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """ Area and Perimeter. """
    def area(self):
        return self.__height * self.__width

    """ Area and Perimeter. """
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
