# What is the greatest product of four numbers in any direction (up, down, left, right, or diagonally) in the 20 x 20 grid?

grid = open('/TheGrid.txt', 'r')

rows = []

def mul(x, y):
	return x * y
	
for line in grid:
	x = line.replace("\n", "")
	row = x.split(",")
	rows.append(row)

numbers = []
for i in range(0, 20):
	for row in rows[0:20:1]:
		for cell in row[i:20:20]: # [col number:20:20]
				numbers.append(int(cell))

rows = []
for i in range(0, 20):
	rows.append(numbers[i::20])

columns = [] # first 20, 20-40, 40-60
for i in range(0, 20):
	columns.append(numbers[20*i:20*i + 20:1])


# go through the rows, multiplying 4 at a time
row_products = []
for row in rows:
	for i in range(0, 19):
		row_products.append(reduce(mul, row[i:i+4:1]))
print "Row Max:", max(row_products)

# do the same thing for the columns
col_products = []
for col in columns:
	for i in range(0, 19):
		col_products.append(reduce(mul, col[i:i+4:1]))
print "Column Max:", max(col_products)

diag1_products = []
for i in range(0, 16):
	for j in range(0, 16):
		diag1_products.append(rows[i][j] * rows[i+1][j+1] * rows[i+2][j+2] * rows[i+3][j+3])

print "Diagonal 1 Max:", max(diag1_products)

diag2_products = []
for i in range(3, 16):
	for j in range(3, 16):
		diag2_products.append(rows[i][j] * rows[i+1][j-1] * rows[i+2][j-2] * rows[i+3][j-3])

print "Diagonal 2 Max:", max(diag2_products)
print rows[12][6] * rows[11][5] * rows[10][4] * rows[9][3]