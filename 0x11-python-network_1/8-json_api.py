#!/usr/bin/python3
"""Error code"""
import requests
import sys


def program():
    """Comment text"""
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    marko = requests.post(url, data={'q': q})
    try:
        polo = marko.json()
        if polo:
            print("[{}] {}".format(polo['id'], polo['name']))
        else:
            print("No result")
    except JSONDecodeError:
        print("Not a valid JSON")


if __name__ == "__main__":
    program()
