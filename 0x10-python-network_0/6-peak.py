#!/usr/bin/python3
"""6. Find a peak"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    n = len(list_of_integers)
    if n == 0:
        return None
    star = 0
    end = n - 1
    while star < end:
        midd = (star + end) // 2
        if list_of_integers[midd] > list_of_integers[midd + 1]:
            end = midd
        else:
            star = midd + 1
    if star == n - 1:
        return list_of_integers[star]
    return list_of_integers[star]
