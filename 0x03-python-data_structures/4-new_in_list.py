#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    listCopy = list(my_list)
    listCopy[idx] = element
    return listCopy
