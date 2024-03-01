#!/usr/bin/python3
"""2. POST an email #0"""
import sys
import urllib.parse as urlP
import urllib.request as urlR


if __name__ == "__main__":
    """
    Sends a POST request to the passed URL with the email as a parameter
    then displays the body of the response
    """
    link = sys.argv[1]
    data = {"email": sys.argv[2]}
    seriData = urlP.urlencode(data).encode("ascii")
    with urlR.urlopen(link, data=seriData) as marko:
        polo = marko.read()
        print(polo.decode())
