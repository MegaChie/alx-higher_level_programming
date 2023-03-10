#!/usr/bin/python3
""" user defined class. """


def add_attribute(a_class, name, value):
    """ Can I? """
    cannot_add = {int, str, float, list, dict, tuple, frozenset, type, object}
    if type(a_class) in cannot_add:
        raise TypeError("can't add new attribute")
    a_class.__setattr__(name, value)
