#!/usr/bin/python3
""" user definned function. """


import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding="utf-8") as fileCreate:
        json.dump(my_obj, fileCreate)
