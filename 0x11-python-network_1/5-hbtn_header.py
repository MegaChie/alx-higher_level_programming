#!/usr/bin/python3
"""What's my status?"""
import requests


def program():
    """Comment text"""
    with requests.get(sys.argv[1]) as polo:
        print(polo.getheader('X-Request-Id'))


if __name__ == "__main__":
    program()
