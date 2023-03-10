#!/usr/bin/python3
""" user defined function. """


def append_after(filename="", search_string="", new_string=""):
    """ Search and update. """
    with open(filename, mode="r+", encoding="utf-8") as readFile:
        temp = readFile.readlines()
    count = 0
    with open(filename, mode="w", encoding="utf-8") as writeFile:
        for lines in temp:
            count += 1
            if search_string in lines:
                temp.insert(count, new_string)
        for lines in temp:
            writeFile.write(lines)
