#!/usr/bin/python3
""" Find a peak """
def find_peak(list_of_integers):
	temp = list(list_of_integers)
	number = 0
	while number != len(temp):
		if number == 0:
			if temp[0] > temp[1]:
				print(temp[0])
		elif number == len(temp) - 1:
			if temp[len(temp) - 1] > temp[number - 1]:
				print(temp[len(temp) - 1])
		else:
			if ((temp[number] > temp[number + 1]) and
				(temp[number] > temp[number - 1])):
				print(temp[number])
		number = number + 1
