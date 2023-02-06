#!/usr/bin/python3
""" user defined class. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle """
    def __init__(self, width, height):
        self.__height = height
        self.__width = width
        super().integer_validator("width", width)
        super().integer_validator("height", height)
