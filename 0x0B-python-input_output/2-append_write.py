#!/usr/bin/python3
""" user definned function. """


def append_write(filename="", text=""):
    """ Append to a file. """
    with open(filename, 'a', "utf-8") as appender:
        appender.write(text)
