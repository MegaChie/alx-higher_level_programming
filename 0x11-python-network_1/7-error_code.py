#!/usr/bin/python3
"""Error code"""
import requests
import sys


def program():
    """Comment text"""
    polo = requests.get(sys.argv[1])
    if polo.code >= 400:
        print("Error code: {}".format(polo.code))


if __name__ == "__main__":
    program()
