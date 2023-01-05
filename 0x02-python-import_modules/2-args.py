#!/usr/bin/python3
if __name__ == "__main__":
	import sys
	argumentVector = sys.argv[1:]
	argumentCount = len(argumentVector)
	count = 1
	if argumentCount == 0:
		print("{} arguments.".format(argumentCount))
	elif argumentCount == 1:
		print("{} argument:".format(argumentCount))
		print("{}: {}".format(count, sys.argv[1]))
	elif argumentCount > 1:
		print("{} arguments:".format(argumentCount))
		while count <= argumentCount:
			print("{}: {}".format(count, sys.argv[count]))
			count = count +1
