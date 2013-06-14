# Find the minimal path sum through the matrix (moving only down and right)
from time import time
start = time()
"""
# get it into triangle form
h = open('/matrix.txt', 'rU')
raw_rows = []
for line in h:
	raw_string = str(line)
	new_string = raw_string.replace("\n", "")
	raw_rows.append(new_string)

rows = []
for row in raw_rows:
	rows.append(row.split(","))
	
top = open('/top_triangle.txt', 'w')

for t in range(80):
	i = t
	j = 0
	while i >= 0 and j <= t:
		top.write(str(rows[i][j]))
		if i > 0:
			top.write(' ')
		j += 1
		i -= 1
	top.write('\n')

bot = open('/bot_triangle.txt', 'w')

for t in range(1, 80):
	i = 79
	j = t
	while i >= t and j <= 79:
		bot.write(str(rows[i][j]))
		if i > t:
			bot.write(' ')
		j += 1
		i -= 1
	bot.write('\n')

'''
0:0
1:0 0:1
2:0 1:1 0:2
3:0 2:1 1:2 0:3

...
80:1 79:2 ... 2:79 1:80
80:77 79:78 78:79 77:80
80:78 79:79 78:80
80:79 79:80
80:80
'''"""
tri = open('/mat_triangle.txt', 'rU')

raw_rows = []
for line in tri:
	raw_string = str(line)
	new_string = raw_string.replace("\n", "")
	raw_rows.append(new_string)

rows = []
for row in raw_rows:
	rows.append(row.split(" "))

for row in rows:
	for index in range(len(row)):
		row[index] = int(row[index])
	
for a in range(1, 159):
	for b in range(len(rows[a])):
		if b == 0 and a < 80:
			rows[a][b] += rows[a-1][0]
		elif (b == a and a < 80):
			rows[a][b] += rows[a-1][b-1]
		elif a < 80:
			if rows[a-1][b-1] > rows[a-1][b]:
				rows[a][b] += rows[a-1][b]
			elif rows[a-1][b-1] < rows[a-1][b]:
				rows[a][b] += rows[a-1][b-1]
			elif rows[a-1][b-1] == rows[a-1][b]:
				print 'equal!'
		elif a >= 80:
			if rows[a-1][b] > rows[a-1][b+1]:
				rows[a][b] += rows[a-1][b+1]
			elif rows[a-1][b] < rows[a-1][b+1]:
				rows[a][b] += rows[a-1][b]
			elif rows[a-1][b] == rows[a-1][b+1]:
				print 'equal!'
print 'Answer:', rows[158][0], 'Processing Time:', time() - start