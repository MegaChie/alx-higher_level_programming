#!/usr/bin/python3
""" user definned function. """


def read_file(filename=""):
    """ Read file """
    with open(filename, encoding="utf-8") as f:
        reader = f.read()
        print(reader, end="")