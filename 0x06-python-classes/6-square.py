#!/usr/bin/python3
""" Defines a square """


class Square:
    """ Coordinates of a square """
    def area(self):
        area = self.__size
        return area * area

    """ Coordinates of a square """
    def size(self):
        return self.__size

    """ Coordinates of a square
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
        print(self.pos_print(), end='')

    """ Coordinates of a square """
    def position(self):
        return self.__position

    """ Coordinates of a square
    args: value - of integer value and is tuple and bigger than 0
          position - tuple representing x and y coordinates """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """ Coordinates of a square """
    def __str__(self):
        self.my_print()

    """ Coordinates of a square
    args: value - of integer value and is bigger or equal to 0 """
    def position(self, value):
        if not type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    """ Coordinates of a square """
    def pos_print(self):
        pos = ""
        if self.size == 0:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos
