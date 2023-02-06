#!/usr/bin/python3
""" user defined function. """


def inherits_from(obj, a_class):
    """ Only sub class of. """
    if not isinstance(obj, a_class) or type(obj) is a_class:
        return False
    else:
        return True
