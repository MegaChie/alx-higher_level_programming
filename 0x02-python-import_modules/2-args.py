#!/usr/bin/python3
if __name__ == "__main__":
	import sys
	argumentVector = sys.argv[1:]
	argumentCount = len(argumentVector)
	count = 1
	if argumentCount == 0:
		print("{argumentCount} arguments.")
	elif argumentCount == 1:
		print("{argumentCount} argument:")
		print("{count}: {sys.argv[1]}")
	elif argumentCount > 1:
		print("{argumentCount} arguments:")
		while count <= argumentCount:
			print("{count}: {sys.argv[count]}")
			count = count +1
