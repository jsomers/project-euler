# http://projecteuler.net/index.php?section=problems&id=90
from time import time
start = time()

SQUARES = ((0, 1), (0, 4), (0, 9), (1, 6), \
			(2, 5), (3, 6), (4, 9), (6, 4), (8, 1))

def has(cube, val):
	if cube.count(str(val)) > 0:
		return 1

def combo(cube1, cube2, a, b):
	if (has(cube1, a) and has(cube2, b)) or (has(cube1, b) and has(cube2, a)):
		return 1
	else:
		return 0

def works(cube1, cube2):
	"Determines if all 9 squares can be made from cube1 and cube2"
	pts = 0
	for square in SQUARES:
		pts += combo(cube1, cube2, square[0], square[1])
	if pts == 9:
		return 1
	else:
		return 0
	
# There are `print (10 * 9 * 8 * 7 / 24) ** 2` = 44,100 possible combos
# Enumerate them:
cubes = []
for a in range(0, 10):
	for b in range(a + 1, 10):
		for c in range(b + 1, 10):
			for d in range(c + 1, 10):
				for e in range(d + 1, 10):
					for f in range(e + 1, 10):
						s = ''.join([str(a), str(b), str(c), \
								str(d), str(e), str(f)])
						# Handle 6, 9 thing.
						if s.count('6') > 0 and s.count('9') == 0: s += '9'
						if s.count('9') > 0 and s.count('6') == 0: s += '6'
						cubes.append(s)

tot = 0
for cube1 in cubes:
	for cube2 in cubes:
		tot += works(cube1, cube2)

print 'Answer:', tot / 2, '\n\n That took', time() - start, 'seconds.'