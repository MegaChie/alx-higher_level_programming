fname = input("Enter file name: ")
with open(fname) as file:
	words = []
	content = file.readlines()
	for line in content:
		temp = line.split()
		for word in temp:
			if word in words:
				continue
			words.append(word)
	print(words)
