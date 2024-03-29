#!/usr/bin/python3
"""3. Error code #0"""
import sys
import urllib.error as urlE
import urllib.parse as urlP
import urllib.request as urlR


if __name__ == "__main__":
    """
    Sends a request to the URL and displays the body of the response
    or displays the error code if the request fails
    """
    link = sys.argv[1]
    try:
        with urlR.urlopen(link) as marko:
            polo = marko.read()
            print(polo.decode())
    except urlE.HTTPError as grab:
        print("Error code: {}".format(grab.code))
