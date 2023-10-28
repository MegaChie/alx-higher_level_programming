#!/usr/bin/python3
""" Find a peak """
def find_peak(list_of_integers):
	i = len(list_of_integers)
	if i <= 6:
		tmp = (list_of_integers)
	elif i > 6:
		tmp = list_of_integers[0:6]
	for n in tmp:
		if n > tmp[index(n) + 1]:
			if n > tmp[index(n) - 1]:
				print(tmp[n])
