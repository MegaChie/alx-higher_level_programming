#!/usr/bin/python3
# comment text


import urllib.request
import urllib.parse
import sys


def program():
    """Comment text"""
    data = parse.urlencode("email": sys.agrv[2])
    req = request.Request(sys.agrv[1], data)
    sent = request.urlopen(req)
    with urllib.request.urlopen(sys.agrv[1], data) as f:
        print(f.read().decode('utf-8'))        


if __name__ == "__main__":
    program()
