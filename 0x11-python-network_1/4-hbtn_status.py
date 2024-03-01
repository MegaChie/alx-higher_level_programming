#!/usr/bin/python3
"""0. What's my status? #0"""
import urllib.request as urlR


if __name__ == "__main__":
    """
    Fetches https://alx-intranet.hbtn.io/status
    and view the body the response body as described
    """
    link = "https://alx-intranet.hbtn.io/status"
    with urlR.urlopen(link) as marko:
        polo = marko.read()
        print("Body response:")
        print("\t- type: {}".format(type(polo)))
        print("\t- content: {}".format(polo))
        print("\t- utf8 content: {}".format(polo.decode()))
