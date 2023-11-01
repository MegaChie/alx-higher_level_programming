#!/usr/bin/python3
# comment text


import urllib.request
import urllib.parse
import sys


def program():
    """Comment text"""
    url = sys.argv[1]
    value = {
    "email":sys.argv[2]
    }
    string = urllib.parse.urlencode(value)
    data = string.encode("ascii")
    with urllib.request.urlopen(url, data) as response:
        text = response.read()
        print(text)
        


if __name__ == "__main__":
    program()
