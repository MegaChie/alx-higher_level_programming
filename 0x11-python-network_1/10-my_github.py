#!/usr/bin/python3
"""9. My GitHub!"""
import sys
import requests as req
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    """
    Takes GitHub credentials and uses the GitHub API to display ID.
    """
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = req.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
        # print(polo.get("id"))
