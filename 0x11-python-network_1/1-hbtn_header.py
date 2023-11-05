#!/usr/bin/python3
"""Response header value"""


import urllib
import sys


def program():
    """Program's code"""
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))


if __name__ == "__main__":
    program()
