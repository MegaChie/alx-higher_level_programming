#!/usr/bin/python3
def common_elements(set_1, set_2):
    copy = list()
    for place in set_1:
        if place in set_2:
            copy.append(place)
        else:
            continue
    return copy
