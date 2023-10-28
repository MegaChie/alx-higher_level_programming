#!/usr/bin/python3
""" Find a peak """
def find_peak(list_of_integers):
	i = len(list_of_integers)
	if i <= 6:
		tmp = list(list_of_integers)
	elif i > 6:
		tmp = list_of_integers[0:6]
	for n in range(len(tmp)):
		if tmp[n] > tmp[n + 1]:
			if tmp[n] > tmp[n - 1]:
				print(tmp[n])
