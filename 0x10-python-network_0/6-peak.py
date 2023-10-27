#!/usr/bin/python3
""" Find a peak """
def find_peak(list_of_integers):
	temp = list(list_of_integers)
	number = 0
	while number != len(temp) - 1:
		if number == 0:
			if temp[number] > temp[number + 1]:
				print(temp[number])
		elif number == len(temp) - 1:
			if temp[number] > temp[number - 1]:
				print(temp[number])
		else:
			if ((temp[number] > temp[number + 1]) and
				(temp[number] > temp[number - 1])):
				print(temp[number])
		number++
