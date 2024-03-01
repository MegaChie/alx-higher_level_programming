#!/usr/bin/python3
"""4. What's my status? #1"""
import requests as req


if __name__ == "__main__":
    """
    Fetches https://alx-intranet.hbtn.io/status using requests library
    and displays the body the response body as described
    """
    link = "https://alx-intranet.hbtn.io/status"
    with req.get(link) as marko:
        polo = marko.text
        print("Body response:")
        print("\t- type: {}".format(type(polo)))
        print("\t- content: {}".format(polo))
