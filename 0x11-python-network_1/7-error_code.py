#!/usr/bin/python3
"""Error code"""
import requests
import sys


def program():
    """Comment text"""
    polo = requests.get(sys.argv[1])
    if polo.status_code >= 400:
        print("Error code: {}".format(polo.status_code))


if __name__ == "__main__":
    program()
