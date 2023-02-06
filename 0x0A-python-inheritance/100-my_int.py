#!/usr/bin/python3
""" user defined class. """


class MyInt(int):
    """ My integer. """
    def __eq__(self, value):
        return super().__ne__(value)

    """ My integer. """
    def __ne__(self, value):
        return super().__eq__(value)
