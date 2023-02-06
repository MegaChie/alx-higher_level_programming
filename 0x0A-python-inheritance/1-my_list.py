#!/usr/bin/python3
""" user defined class. """


class MyList(list):
    """ My list. """
    def print_sorted(self):
        print(sorted(self))
