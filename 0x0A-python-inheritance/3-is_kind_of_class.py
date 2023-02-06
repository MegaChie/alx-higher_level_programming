#!/usr/bin/python3
""" user defined function. """


def is_kind_of_class(obj, a_class):
    """ Same class or inherit from. """
    if type(obj) is a_class or isinstance(obj, a_class) is True:
        return True
    else:
        return False
