#!/usr/bin/python3
"""Error code #0"""
import urllib.request
import urllib.parse
import sys


def program():
    """Comment text"""
    try:
        with urllib.request.urlopen(sys.argv[1]) as answer:
            html = response.read()
            print(html.decode("utf-8"))
    except HTTPError as fetal:
        print("Error code: {}".format(fetal.code))


if __name__ == "__main__":
    program()
