#!/usr/bin/python3
"""What's my status?"""
import requests


def program():
    """Comment text"""
    answer = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(answer.text)))
    print("\t- content: {}".format(answer.text))


if __name__ == "__main__":
    program()
