#!/usr/bin/python3
"""My GitHub!"""
import requests
from requests.auth import HTTPBasicAuth
import sys


def program():
    """Comment text"""
    name, pkey = sys.argv[1], sys.argv[2]
    marko = requests.get("https://api.github.com/user",
        auth=(HTTPBasicAuth(name, pkey)))
    polo = marko.json()
    if polo:
        print(polo['id'])
    else:
        print("None")


if __name__ == "__main__":
    program()
