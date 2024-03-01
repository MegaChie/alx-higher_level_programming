#!/usr/bin/python3
"""7. Error code #1"""
import sys
import requests as req


if __name__ == "__main__":
    """
    Sends a request to the URL and displays the body of the response
    or displays the error code if the request fails using requests library
    """
    link = sys.argv[1]
    with req.get(link) as marko:
        if marko.status_code >= 400:
            print("Error code: {}".format(marko.status_code))
        else:
            polo = marko.text
            print(polo)
