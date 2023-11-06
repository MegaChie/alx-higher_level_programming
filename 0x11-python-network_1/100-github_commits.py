#!/usr/bin/python3
"""Time for an interview!"""
import requests
import sys


def program():
    """Comment text"""
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2],
                                                              sys.argv[1])
    marko = requests.get(url)
    try:
        polo = marko.json()
        for i in range(10):
            print("{}: {}".format(polo[i]['sha'],
                                  polo[i]['commit']['author']['name']))
    except IndexError:
        pass


if __name__ == "__main__":
    program()
