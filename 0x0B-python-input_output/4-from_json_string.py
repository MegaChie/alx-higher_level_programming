#!/usr/bin/python3
""" user definned function. """


import json


def from_json_string(my_str):
    """ From JSON string to Object """
    return json.loads(my_str)
