#!/usr/bin/python3
# comment text


import urllib.request
import urllib.parse
import sys


def program():
    """Comment text"""
    sent = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(sent)
    data = data.encode("ascii")
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as answer:
        html = answer.read()
        print(html.decode("utf-8"))


if __name__ == "__main__":
    program()
