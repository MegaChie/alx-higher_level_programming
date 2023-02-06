#!/usr/bin/python3
""" user defined class. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Full rectangle. """
    def __init__(self, width, height):
        self.__height = height
        self.__width = width
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    """ Full rectangle. """
    def area(self):
        return self.__height * self.__width

    """ Full rectangle. """
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
