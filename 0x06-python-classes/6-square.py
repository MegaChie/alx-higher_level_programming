#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Access and update private attribute """
    def area(self):
        area = self.__size
        return area * area

    """ Access and update private attribute """
    def size(self):
        return self.__size

    """ Access and update private attribute
    args: value - of integer value and is bigger or equal to 0 """
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """ Coordinates of a square """
    def my_print(self):
        size = self.__size
        nl = self.__position[1]
        ws = self.__position[0]
        if size == 0:
            print()
        for newlines in range(nl):
            print()
        for row in range(size):
            print((' ' * ws) + ('#' * size))

    """ Coordinates of a square """
    def position(self):
        return self.__position

    """ Coordinates of a square
    args: value - of integer value and is tuple and bigger than 0 """
    def position(self, value):
        text = 'position must be a tuple of 2 positive integers'
        if type(value) is not tuple or len(value) != 2:
            raise TypeError(text)
        for place in value:
            if type(place) is not int or place < 0:
                raise TypeError(text)
        self.__position = value

    """ Coordinates of a square
    args: value - of integer value and is tuple and bigger than 0
          position - tuple representing x and y coordinates """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
