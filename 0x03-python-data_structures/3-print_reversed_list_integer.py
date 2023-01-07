#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    place = len(my_list) - 1
    while place > -1:
        print("{}".format(my_list[place]))
        place -= 1
