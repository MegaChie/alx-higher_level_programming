#!/usr/bin/python3
""" Find a peak """
def find_peak(list_of_integers):
	i = len(list_of_integers)
	tmp = (list_of_integers)
	for n in tmp:
		if n > tmp[tmp.index(n) + 1]:
			if n > tmp[tmp.index(n) - 1]:
				print(n)
		if n == tmp[-1]:
			pass
