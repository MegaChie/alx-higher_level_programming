#!/usr/bin/python3
# comment text


import urllib.request
import urllib.parse
import sys


def program():
    """Comment text"""
    data = urllib.parse.urlencode({"a_key": sys.argv[2]})
    data = data.encode('ascii')
    url = sys.argv[1]
    response = urllib.request.urlopen(url, data)
    with urllib.request.urlopen(url, data) as response:
        print(response.info())
        


if __name__ == "__main__":
    program()
