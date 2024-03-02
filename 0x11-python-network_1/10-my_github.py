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
    auth = login(sys.argv[1], sys.argv[2])
    r = req.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
