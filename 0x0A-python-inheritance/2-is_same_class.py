#!/usr/bin/python3
""" user defined function. """


def is_same_class(obj, a_class):
    """ Exact same object. """
    if type(obj) is a_class:
        return True
    else:
        return False
