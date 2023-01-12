#!/usr/bin/python3
def uniq_add(my_list=[]):
    backup = list()
    addup = 0
    for place in my_list:
        if place not in backup:
            backup.append(place)
        else:
            continue
    for holder in backup:
        addup += holder
    return addup
