#!/usr/bin/python3
"""9. My GitHub!"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    name, pkey = sys.argv[1], sys.argv[2]
    marko = requests.get("https://api.github.com/user",
                         auth=(HTTPBasicAuth(name, pkey)))
    try:
        polo = marko.json()
        print(polo['id'])
    except:
        print("None")
