#!/usr/bin/python3
# comment text


import urllib.request
import sys


def execute():
    """Comment text"""
    with urllib.request.urlopen(sys.argv[1]) as response:
        line = response.info()
        print(line["X-Request-Id"])


if __name__ == "__main__":
    execute()
