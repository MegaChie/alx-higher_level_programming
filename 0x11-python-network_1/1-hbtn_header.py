#!/usr/bin/python3
"""1. Response header value #0"""
import sys
import urllib.request as urlR


if __name__ == "__main__":
    """
    Sends a request to the URL and displays the value of the X-Request-Id
    """
    link = sys.argv[1]
    with urlR.urlopen(link) as marko:
        polo = marko.headers
        print(polo.get("X-Request-Id"))
