#!/usr/bin/python3
""" user definned function. """


import json


def load_from_json_file(filename):
    """ Create object from a JSON file """
    with open(filename, 'r', encoding="utf-8") as fileLoader:
        return json.load(fileLoader)
