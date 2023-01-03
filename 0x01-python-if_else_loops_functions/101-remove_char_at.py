#!/usr/bin/python3
def remove_char_at(str, n):
    for place in range(len(str)):
        if place != n:
            continue
        elif place == n:
            str[place] = ""
    return str
