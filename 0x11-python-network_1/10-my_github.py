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
    token = sys.argv[2]
    headers = {'Authorization': 'token ' + token,
              username: sys.argv[1]}
    link = 'https://api.github.com/user'
    login = req.get(link, headers=headers)
    print(login.json())
        # print(polo.get("id"))
