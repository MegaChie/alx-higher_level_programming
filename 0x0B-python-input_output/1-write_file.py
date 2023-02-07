#!/usr/bin/python3
""" user definned function. """


def write_file(filename="", text=""):
    """ Write to a file """
    with open(filename, 'w', encoding="utf-8") as writer:
        writer.write(text)
        return len(text)
