#!/usr/bin/python3
""" user definned function. """


import json


def class_to_json(obj):
    """ Class to JSON """
    return obj.__dict__
