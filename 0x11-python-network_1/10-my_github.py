#!/usr/bin/python3
"""9. My GitHub!"""
import sys
import requests as req
from requests.auth import HTTPBasicAuth as login


if __name__ == "__main__":
    """
    Takes GitHub credentials and uses the GitHub API to display ID.
    """
    # username
    name = sys.argv[1]
    # password
    phra = sys.argv[2]
    link = "https://api.github.com/user"
    with req.get(link, auth=(login(username: name, password: phra))) as marko:
        polo = marko.json()
        print(polo)
        # print(polo.get("id"))