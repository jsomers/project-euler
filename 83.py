""" Project Euler problem #83 (problem statement: http://projecteuler.net/print.php?id=83)
Approach: Keep two matrices, one with accruing minimal path sums and the other for marking cells.
All cells but (0, 0) are marked '0' initially. Proceeding outwards towards the bottom right corner,
(the exact motion is in the 'pairs' list), find the minimal path sum from some cell to a marked cell,
then mark that cell. E.g., the least costly path from (1, 0) to (0, 0) is direct, so you simply 
add the two cells: 1096 + 4445 = 5541. (1, 0) becomes 5541, and it is marked '1'.

To find the actual minimal path we must try a variety of routes (a 'heuristics' approach) which are shown below.
"""
# Keep track of time :)
from time import time
start = time()

# Get the matrix.
matrix = []
for l in file('/Users/jsomers/Documents/Work/Project Euler/matrix.txt','rt'):
	matrix.append([int(x) for x in l.split(',')])

# Another copy of the matrix (used in the find_route function)
copy = []
for l in file('/Users/jsomers/Documents/Work/Project Euler/matrix.txt','rt'):
	copy.append([int(x) for x in l.split(',')])

# Marker matrix. Ugly because [[0]*80]*80 can only store 80 unique values!
summed = [[0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80]
summed[0][0] = 1
marker2 = [[0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80, [0]*80]

# Routes.
direct_left = ['left']
one_up_and_left = ['up', 'left']
one_down_and_left = ['down', 'left']
wrap_around_up = ['right', 'up', 'up', 'left', 'left']
whole_right_package = [one_down_and_left, one_up_and_left, wrap_around_up, direct_left]

direct_up = ['up']
one_left_and_up = ['left', 'up']
one_right_and_up = ['right', 'up']
wrap_around_right = ['down', 'right', 'right', 'up', 'up']
whole_left_package = [one_right_and_up, one_left_and_up, direct_up]

corner_package = [wrap_around_right, direct_up, direct_left]


# Helper function.
def take_route(route, a, b, count, total):
	""" Feed this function one of the above routes. The
	conditions here make sure (a) we finish on a marked
	square and (b) we don't go out of bounds.
	
	>> print take_route(direct_left, 4, 5, 0, matrix[4][5])
	61697
	"""
	if a < 0 or b < 0:
		return 10**6 # "invalidating" the route (10^6 couldn't possibly be a best path).
	if count == len(route) and summed[a][b] > 0:
		return total
	elif count == len(route) and summed[a][b] == 0:
		return 10**6
	direction = route[count]
	if direction == 'up':
		if a-1 >= 0 and b >= 0 and a-1 <= 79 and b <= 79:
			if summed[a-1][b] > 0:
				total += matrix[a-1][b]
				return total
			else:
				total += matrix[a-1][b]
				return take_route(route, a-1, b, count+1, total)
		else:
			return 10**6
	elif direction == 'down':
		if a+1 >= 0 and b >= 0 and a+1 <= 79 and b <= 79:
			if summed[a+1][b] > 0:
				total += matrix[a+1][b]
				return total
			else:
				total += matrix[a+1][b]
				return take_route(route, a+1, b, count+1, total)
		else:
			return 10**6
	elif direction == 'left':
		if a >= 0 and b-1 >= 0 and a <= 79 and b-1 <= 79:
			if summed[a][b-1] > 0:
				total += matrix[a][b-1]
				return total
			else:
				total += matrix[a][b-1]
				return take_route(route, a, b-1, count+1, total)
		else:
			return 10**6
	elif direction == 'right':
		if a >= 0 and b+1 >= 0 and a <= 79 and b+1 <= 79:
			if summed[a][b+1] > 0:
				total += matrix[a][b+1]
				return total
			else:
				total += matrix[a][b+1]
				return take_route(route, a, b+1, count+1, total)
		else:
			return 10**6

def go(a, b, route):
	return take_route(route, a, b, 0, matrix[a][b])

pairs = []
for a in range(1, 80):
	b = 0
	while a != b:
		pairs.append((a, b))
		pairs.append((b, a))
		b += 1
	if a == b:
		pairs.append((a, b))
""" >> print pairs
	[(1, 0), (0, 1), (1, 1), (2, 0), (0, 2), (2, 1), (1, 2), (2, 2), (3, 0), (0, 3), (3, 1), (1, 3) ... ]
"""

for pair in pairs:
	a, b = pair[0], pair[1]
	""" Three cases: 
			a > b: you're on the bottom left
			b > a: you're on the top right
			a == b: you're at a corner
	"""
	if a >= 79 and b >= 79:
		print 'answer:', matrix[79][79] + min([matrix[79][78], matrix[78][79]]), 'time:', '%.3f' %( time() - start ), 'seconds'
	if a > b:
		options = []
		for route in whole_left_package:
			options.append(go(a, b, route)) # Find a partial shortest path.
		matrix[a][b] = min(options) # This cell now becomes the best path.
		summed[a][b] = 1 # Mark the cell.
	elif b > a:
		options = []
		for route in whole_right_package:
			options.append(go(a, b, route))
		matrix[a][b] = min(options)
		summed[a][b] = 1
	elif a == b:
		options = []
		for route in corner_package:
			options.append(go(a, b, route))
		matrix[a][b] = min(options)
		summed[a][b] = 1

# An ugly function to reverse engineer the actual route (instead of the sum). Useful for debugging/curiosity.
def find_route(a, b, route):
	if a == 0 and b == 0:
		print "The Route:", route
		return
	marker2[a][b] = 1
 	up, down, left, right = 10**6, 10**6, 10**6, 10**6
	if a + 1 <= 79:
		if marker2[a+1][b] == 0:
			down = matrix[a+1][b]
	if a - 1 >= 0:
		if marker2[a-1][b] == 0:
			up = matrix[a-1][b]
	if b + 1 <= 79:
		if marker2[a][b+1] == 0:
			right = matrix[a][b+1]
	if b - 1 >= 0:
		if marker2[a][b-1] == 0:
			left = matrix[a][b-1]
	options = [up, down, right, left]
	best = min(options)
	if best == up:
		route.append(copy[a-1][b])
		return find_route(a-1, b, route)
	if best == down:
		route.append(copy[a+1][b])
		return find_route(a+1, b, route)
	if best == left:
		route.append(copy[a][b-1])
		return find_route(a, b-1, route)
	if best == right:
		route.append(copy[a][b+1])
		return find_route(a, b+1, route)

find_route(79, 79, [copy[79][79]])