#!/usr/bin/python3
""" Find a peak """
def find_peak(list_of_integers):
	temp = list(list_of_integers)
	temp.sort()
	print(temp[-1])
