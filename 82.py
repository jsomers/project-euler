from time import time
start = time()
matrix = []
for l in file('/matrix.txt','rt'):
	matrix.append([int(x) for x in l.split(',')])

def col_calc(b):
	news = [0]*80
	if b == -1:
		things = []
		for a in range(80):
			things.append(matrix[a][0])
		print min(things), time() - start
		return
	for a in range(80):
		me = matrix[a][b]
		UP, TWO_UP, THREE_UP, DOWN, TWO_DOWN, THREE_DOWN, NEXT = 10**10, 10**10, 10**10, 10**10, 10**10, 10**10, 10**10
		NEXT = sum([me, matrix[a][b+1]])
		if a >= 1:
			up = matrix[a-1][b]
			up_next = matrix[a-1][b+1]
			UP = sum([me, up, up_next])
		if a >= 2:
			two_up = matrix[a-2][b]
			two_up_next = matrix[a-2][b+1]
			TWO_UP = sum([me, up, two_up, two_up_next])
		if a >= 3:
			three_up = matrix[a-3][b]
			three_up_next = matrix[a-3][b+1]
			THREE_UP = sum([me, up, two_up, three_up, three_up_next])
		if a <= 78:
			down = matrix[a+1][b]
			down_next = matrix[a+1][b+1]
			DOWN = sum([me, down, down_next])
		if a <= 77:
			two_down = matrix[a+2][b]
			two_down_next = matrix[a+2][b+1]
			TWO_DOWN = sum([me, down, two_down, two_down_next])
		if a <= 76:
			three_down = matrix[a+3][b]
			three_down_next = matrix[a+3][b+1]
			THREE_DOWN = sum([me, down, two_down, three_down, three_down_next])
		news[a] = min([UP, TWO_UP, DOWN, TWO_DOWN, THREE_UP, THREE_DOWN, NEXT])
	for a in range(80):
		matrix[a][b] = news[a]

for i in range(78, -2, -1):
	col_calc(i)