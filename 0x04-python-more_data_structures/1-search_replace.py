#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for place in range(len(my_list)):
        if my_list[place] == search:
            my_list[place] = replace
        else:
            continue
