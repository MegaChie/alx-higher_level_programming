#!/usr/bin/python3
""" Find a peak """


def find_peak(list_of_integers):
    """ look for a peak in the given list """
    n = len(list_of_integers)
    tmp = list_of_integers.sort()
    print(tmp[-1])
