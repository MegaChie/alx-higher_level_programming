#!/usr/bin/python3
"""POST an email"""
import requests
import sys


def program():
    """Comment text"""
    data = {'email': sys.argv[2]}
    polo = requests.post(sys.argv[1], data=data)
    print(polo.text)


if __name__ == "__main__":
    program()
