#!/usr/bin/python3
# comment text


import urllib.request
import urllib.parse
import sys


def program():
    """Comment text"""
    try:
        with urllib.request.urlopen(sys.argv[1]) as answer:
            html = response.read()
            print(html.decode("utf-8"))
    except urllib.error.HTTPError as fetal:
        print("Error code: {}".format(fetal.code))


if __name__ == "__main__":
    program()
