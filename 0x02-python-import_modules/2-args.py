#!/usr/bin/python3
if __name__ == "__main__":
	import sys
	argumentVector = sys.argv[1:]
	argumentCount = len(argumentVector)
	count = 1
	if argumentCount == 0:
		print(f"{argumentCount} arguments.")
	elif argumentCount == 1:
		print(f"{argumentCount} argument:")
		print(f"{count}: {sys.argv[1]}")
	elif argumentCount > 1:
		print(f"{argumentCount} arguments:")
		while count <= argumentCount:
			print(f"{count}: {sys.argv[count]}")
			count = count +1
