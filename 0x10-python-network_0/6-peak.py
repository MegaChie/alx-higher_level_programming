#!/usr/bin/python3
""" Find a peak """
def find_peak(list_of_integers):
	temp = list(list_of_integers)
	for number in temp:
		if (number > number + 1) and (number > number -1):
			print (number)
