import time, math
start = time.time()

# Solve the Pell equation x^2 - 3y^2 = 1. See http://mathschallenge.net/index.php?section=problems&show=true&titleid=almost_equilateral_triangles&full=true#solution
sols = [(2, 1)]
i = 0
while i < 20:
	x_i, y_i = sols[-1][0], sols[-1][1]
	sols.append((2 * x_i + 3 * y_i, 2 * y_i + x_i))
	i += 1

# a = (2x +- 1) / 3.
def get_a(x, switch):
	if switch:
		return (2 * x + 1) / 3.
	else:
		return (2 * x - 1) / 3.

# Get a's for each x, then get perimeter and append to a list.
perims = []
for s in sols:
	swch = s[0] % 2
	the_a = get_a(s[0], swch)
#	print swch, int(the_a)
	if swch:
		perims.append(3 * the_a + 1)
	else:
		perims.append(3 * the_a - 1)

perims.pop(0)
#print int(sum(perims[:17]))

#for p in perims:
#	print p, p < 10 ** 9

#print perims[:14]
print int(sum(perims[:14]))
#7220496866
#7220496868