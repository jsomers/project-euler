h = open('/names.txt', 'r')

for line in h:
	raw = str(line)
	new = raw.replace('"', '')
	names = new.split(',')

names.sort()
names.insert(0, '') # make sure the index starts at 1, not zero

A_count = 0

scores = []

for index in range(len(names)):
	word_worth = 0
	string = names[index]
	letterlist = list(string)
	print letterlist
	for letter in letterlist:
		if letter == 'A':
			word_worth += 1
		elif letter == 'B':
			word_worth += 2
		if letter == 'C':
			word_worth += 3
		elif letter == 'D':
			word_worth += 4
		if letter == 'E':
			word_worth += 5
		elif letter == 'F':
			word_worth += 6
		if letter == 'G':
			word_worth += 7
		elif letter == 'H':
			word_worth += 8
		if letter == 'I':
			word_worth += 9
		elif letter == 'J':
			word_worth += 10
		if letter == 'K':
			word_worth += 11
		elif letter == 'L':
			word_worth += 12
		if letter == 'M':
			word_worth += 13
		elif letter == 'N':
			word_worth += 14
		if letter == 'O':
			word_worth += 15
		elif letter == 'P':
			word_worth += 16
		elif letter == 'Q':
			word_worth += 17
		if letter == 'R':
			word_worth += 18
		elif letter == 'S':
			word_worth += 19
		if letter == 'T':
			word_worth += 20
		elif letter == 'U':
			word_worth += 21
		if letter == 'V':
			word_worth += 22
		elif letter == 'W':
			word_worth += 23
		if letter == 'X':
			word_worth += 24
		elif letter == 'Y':
			word_worth += 25
		elif letter == 'Z':
			word_worth += 26
	word_score = word_worth * index
	scores.append(word_score)

print sum(scores)