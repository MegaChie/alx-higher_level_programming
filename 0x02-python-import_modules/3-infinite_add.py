#!/usr/bin/python3
import sys
argumentVector = sys.argv[1:]
argumentCount = len(argumentVector)
count = 1
result = 0
while count <= argumentCount:
	result += int(sys.argv[index])
	count += 1
print("{}".format(result))
