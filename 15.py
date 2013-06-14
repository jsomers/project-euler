# How many paths are there from the top left corner of a 20 x 20 grid to the bottom right corner?
# This needs to be iterative, it's taking way way too long

from time import time
start = time()

# very fast, based on the central binomial coefficient
def mul(x, y):
	return x*y
	
def fact(n):
	facts = []
	for i in range (1, n+1):
		facts.append(i)
	a = reduce(mul, facts)
	return a

print fact(4)

def routes(n):
	return fact(2*n)/(fact(n)**2)
	
print routes(20	)

function

''' # A slow recursive algorithm:
ct = 0

def mover(x, y):
	if x == 0 and y == 0:
		global ct
		ct += 1
	elif x > 0 and y > 0:
		mover(x-1, y)
		mover(x, y-1)
	elif x == 0 and y > 0:
		mover(x, y-1)
	elif x > 0  and y == 0:
		mover(x-1, y)

mover(9, 9)
print ct
'''

print "Time: ", '%2d' %(time() - start), "seconds"