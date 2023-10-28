#!/usr/bin/python3
""" Find a peak """
def find_peak(list_of_integers):
	i = len(list_of_integers)
	if i <= 5:
		tmp = list(list_of_integers)
	elif i > 5:
		tmp = list_of_integers[0:5]
	print(list_of_integers)
	print(tmp)
