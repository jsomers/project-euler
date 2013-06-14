# http://projecteuler.net/index.php?section=problems&id=91

""" We account for four types of triangle: those with points on the x- and
y-axes (opposites), those with a perpendicular projection to one of the axes
(projections), those with a leg extending directly diagonal away from the 
origin (diagonals), and everything else (internals).

"""


from time import time
start = time()

def gcd(a, b):
    while a:
        a, b = b % a, a
    return b

def opposite_edges(n):
	return n ** 2

def projections(n):
	return n ** 2 * 2

def diagonals(n):
	a = n // 2
	if n % 2:
		return 4 * sum(range(a + 1))
	else:
		return 2 * (sum(range(a + 1)) + sum(range(a)))

def internal_step(x, y, n):
	X, Y = x, y
	t = 0
	a, b = x / gcd(x, y), y / gcd(x, y)
	while x + b <= n and y - a >= 0:
		x += b
		y -= a
		t += 1
	x, y = X, Y
	while x - b >= 0 and y + a <= n:
		x -= b
		y += a
		t += 1
	return 2 * t

def internals(n):
	t = 0
	for x in range(1, n + 1):
		for y in range(x + 1, n + 1):
			t += internal_step(x, y, n)

	return t

def right_triangles(n):
	return opposite_edges(n) + projections(n) + diagonals(n) + internals(n)

print 'Answer:', right_triangles(50), '\n\n That took', time() - start, 'seconds'