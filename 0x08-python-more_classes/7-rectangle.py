#!/usr/bin/python3
""" More Classes and Objects """


class Rectangle:
    """ Change representation. """
    number_of_instances = 0
    print_symbol = '#'

    @property
    def width(self):
        return self.__width

    """ Change representation.
    args: value - of integer  type """
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ Change representation. """
    @property
    def height(self):
        return self.__height

    """ Change representation. """
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ Change representation.
    Args: width - of integer type
          height - of integer type """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol

    """ Change representation. """
    def area(self):
        return self.__height * self.__width

    """ Change representation. """
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    """ Change representation. """
    def __str__(self):
        printed = ""
        if self.__height == 0 or self.__width == 0:
            return printed
        for raw in range(self.__height):
            for collmun in range(self.__width):
                printed += str(self.print_symbol)
            if raw != self.__height - 1:
                printed += '\n'
        return printed

    """ Change representation. """
    def __repr__(self):
        first = str(self.__width)
        second = str(self.__height)
        result = "Rectangle(" + first + ", " + second + ")"
        return result

    """ Change representation. """
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
