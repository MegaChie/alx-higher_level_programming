#!/usr/bin/python3
"""6. POST an email #1"""
import sys
import requests as req


if __name__ == "__main__":
    """
    Sends a POST request to the passed URL with the email as a parameter
    then displays the body of the response.
    This time it uses requests library.
    """
    link = sys.argv[1]
    data = {"email": sys.argv[2]}
    with req.post(link, data=data) as marko:
        polo = marko.text
        print(polo)
