h = open('/triangle.txt', 'r')

rows = []

for line in h:
	x = line.replace("\n", "")
	row = x.split(" ")
	rows.append(row)
	
for row in rows:
	print max(row)


# Calculate expected value of things you leave off by taking a certain turn

# Superimposed Pascal triangle is the number of routes that go to that point

# Answer by pen-and-paper is 1074