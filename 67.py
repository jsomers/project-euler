# Using an efficient algorithm find the maximal sum in the triangle? mather's method, problem 18
t = open('/triangle.txt', 'rU')

raw_rows = []
for line in t:
	raw_string = str(line)
	new_string = raw_string.replace("\n", "")
	raw_rows.append(new_string)

rows = []
for row in raw_rows:
	rows.append(row.split(" "))

for row in rows:
	for index in range(len(row)):
		row[index] = int(row[index])

for n in range(98, -1, -1):
	theRow = rows[n]
	belowMe = rows[n+1]
	for i in range(len(theRow)):
		if belowMe[i] > belowMe[i+1]:
			theRow[i] += belowMe[i]
		elif belowMe[i] <= belowMe[i+1]:
			theRow[i] += belowMe[i+1]

print rows[0]