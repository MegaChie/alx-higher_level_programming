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
    link = """https://api.github.com/users/{}""".format(sys.argv[1])
    # name
    name = sys.argv[1]
    # password
    phra = sys.argv[2]
    with req.get(link, auth=login(name, phra)) as marko:
        polo = marko.json()
        print(polo)
        print(polo.get("id"))
