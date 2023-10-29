#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    """ look for a peak in the given list """
    n = len(list_of_integers)
    if n == 0:
        return None
    start = 0
    end = n - 1
    while start < end:
        mid = (start + end) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            end = mid
        else:
            start = mid + 1
    if start == n - 1:
        return list_of_integers[start]
    return list_of_integers[start]
