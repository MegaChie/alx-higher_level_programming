#!/usr/bin/python3
"""3. Error code #0"""
import sys
import urllib.parse as urlP
import urllib.request as urlR


if __name__ == "__main__":
    """
    sends a request to the URL and displays the body of the response
    """
    link = sys.argv[1]
    with urlR.urlopen(link) as marko:
    try:
        with urlR.urlopen(link) as marko:
            polo = marko.read()
            print(polo.decode())
    except urllib.error.HTTPError as grab:
        print("Error code: {}".fromat(grab.code))
