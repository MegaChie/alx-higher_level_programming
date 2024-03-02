#!/usr/bin/python3
"""10. Time for an interview!"""
import sys
import requests as req

if __name__ == "__main__":
    """
    Takes 2 arguments, repository name and owner name
    and displays last commit IDs and names of commiters
    """
    link = """https://api.github.com/repos/{}/{}/commits""".format(sys.argv[2],
                                                                   sys.argv[1])
    with req.get(link) as marko:
        polo = marko.json()
        try:
            for i in range(10):
                print("{}: {}".format(polo[i]["sha"],
                                      polo[i]["commit"]["author"]["name"]))
        except IndexError:
            pass
