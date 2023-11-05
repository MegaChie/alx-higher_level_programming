#!/usr/bin/python3
"""What's my status?"""
import requests
import sys


def program():
    """Comment text"""
    polo = requests.get(sys.argv[1])
    print(polo.headers('X-Request-Id'))


if __name__ == "__main__":
    program()
