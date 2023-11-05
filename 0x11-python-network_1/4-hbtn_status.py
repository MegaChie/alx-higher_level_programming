#!/usr/bin/python3
"""What's my status?"""
import requests


def program():
    """Comment text"""
    answer = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(answer)))
    print("\t- content: {}".format(answer))


if __name__ == "__main__":
    program()
