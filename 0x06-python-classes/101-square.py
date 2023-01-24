#!/usr/bin/python3
""" square """


class Square:
    """ Print Square instance """
    def __str__(self):
        return self.pos_print()[:-1]

    """ Print Square instance
    args: size - integer value grater than or equal to 0
          position - tuple value is equal to or grater than 0 that makeup
          x and y coordinates """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    """ Print Square instance """
    def size(self):
        return self.__size

    """ Print Square instance
    args: value - integer value grater or equal to 0 """
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    """ Print Square instance """
    def position(self):
        return self.__position

    """ Print Square instance
    args: value - integer value grater or equal to 0 """
    def position(self, value):
        if type(value) is not tuple:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    """ Print Square instance """
    def area(self):
        return self.__size * self.__size

    """ Print Square instance """
    def pos_print(self):
        pos = ""
        if not self.size:
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

    """ Print Square instance """
    def my_print(self):
        print(self.pos_print(), end="")
