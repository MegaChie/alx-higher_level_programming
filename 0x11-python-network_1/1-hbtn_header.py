#!/usr/bin/python3
# comment text


import urllib.request
import sys


def program():
    """Comment text"""
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))


if __name__ == "__main__":
    program()