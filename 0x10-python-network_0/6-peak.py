#!/usr/bin/python3
""" Find a peak """
def find_peak(list_of_integers):
	list_of_integers.sort()
	print(list_of_integers[-1])
