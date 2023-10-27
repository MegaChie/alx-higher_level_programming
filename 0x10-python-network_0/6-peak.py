#!/usr/bin/python3
""" Find a peak """
def find_peak(list_of_integers):
	temp = list(list_of_integers)
	for place in range(len(temp)):
		if (place == 0) and (temp[place] > temp[place + 1]):
			print (temp[place])
		else if (place == len(temp) - 1) and (temp[place] > temp[place - 1]):
			print (temp[place])
		else:
			if ((temp[place] > temp[place - 1]) and (temp[place] > temp[place + 1])):
				print (temp[place])
