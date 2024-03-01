#!/usr/bin/python3
"""8. Search API"""
import json
import sys
import requests as req


if __name__ == "__main__":
    """
    Sends a POST request url with a letter as a parameter and returns either:
    - Not a valid JSON.
    - Name and ID of the person whos name starts with the letter
    """
    link = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 2:
        data = {"q": sys.argv[1]}
    else:
        data = {"q": ""}
    with req.post(link, data=data) as marko:
        try:
            polo = marko.json()
            if polo:
                print("[{}] {}".format(polo.get("id"), polo.get("name")))
            else:
                print("No result")
        except JSONDecodeError:
            print("Not a valid JSON")
