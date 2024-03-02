#!/usr/bin/python3
"""10. Time for an interview!"""
import sys
import requests as req

if __name__ == "__main__":
    """
    Takes 2 arguments, repository name and owner name
    and displays last commit IDs and names of commiters
    """
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    r = req.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
