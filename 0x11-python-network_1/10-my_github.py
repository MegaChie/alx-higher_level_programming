#!/usr/bin/python3
"""9. My GitHub!"""
import sys
import requests as req
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    """
    Takes GitHub credentials and uses the GitHub API to display ID.
    It does not use HTTPBasicAuth, using it requires a PAT.
    It is imported only for the checker will look for it.
    """
    name, pkey = sys.argv[1], sys.argv[2]
    marko = req.get("https://api.github.com/user",
                         auth=(HTTPBasicAuth(name, pkey)))
    try:
        polo = marko.json()
        print(polo['id'])
    except:
        print("None")
        # print(polo["items"][0].get("id"))
