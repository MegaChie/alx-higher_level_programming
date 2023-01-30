#!/usr/bin/python3
""" More Classes and Objects """


class Rectangle:
    """ Compare rectangles. """
    number_of_instances = 0
    print_symbol = '#'

    @property
    def width(self):
        return self.__width

    """ Compare rectangles.
    args: value - of integer  type """
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """ Compare rectangles. """
    @property
    def height(self):
        return self.__height

    """ Compare rectangles. """
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """ Compare rectangles.
    Args: width - of integer type
          height - of integer type """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol

    """ Compare rectangles. """
    def area(self):
        return self.__height * self.__width

    """ Compare rectangles. """
    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    """ Compare rectangles. """
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

    """ Compare rectangles. """
    def __repr__(self):
        first = str(self.__width)
        second = str(self.__height)
        result = "Rectangle(" + first + ", " + second + ")"
        return result

    """ Compare rectangles. """
    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    """ Compare rectangles.
    Args: rect_1 - instance of Rectangle class
          rect_2 - instance of Rectangle class """
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
