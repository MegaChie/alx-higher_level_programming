#!/usr/bin/python3
"""5. Response header value #1"""
import sys
import requests as requ


if __name__ == "__main__":
    """
    Sends a request to the URL and displays the value of the X-Request-Id
    but this time it uses requests library.
    """
    link = sys.argv[1]
    with requ.get(link) as marko:
        polo = marko.headers
        print(polo.get("X-Request-Id"))
