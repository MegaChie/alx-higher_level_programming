#!/usr/bin/python3
""" 0x0C. Python - Almost a circle """


class Base:
    __nb_objects = 0
    """ Base class """
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
