#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    merger = list()
    differ = list()
    for place in set_1:
        merger.append(place)
    for place in set_2:
        merger.append(place)
    for place in merger:
        if place in set_1 and place in set_2:
            continue
        else:
            differ.append(place)
    return differ
