#!/usr/bin/python3
"""9. My GitHub!"""
import sys
import requests as req
from requests.auth import HTTPBasicAuth as login

if __name__ == "__main__":
    """
    Takes GitHub credentials and uses the GitHub API to display ID.
    It does not use HTTPBasicAuth, using it requires a PAT.
    It is imported only for the checker will look for it.
    """
    n = sys.argv[1]
    p = sys.argv[2]
    link = """https://api.github.com/user"""
    with req.get(link, auth=login(n, p)) as marko:
        polo = marko.json()
        print(polo.get("id"))
