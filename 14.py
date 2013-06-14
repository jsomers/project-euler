# Which starting number 837799 (under one million) for the Collatz problem produces the longest chain?... 524 steps!
from time import time
h = open('/collatz.txt', 'w')
start = time()
step_counts = []
def update(n, count):
	if n % 2 == 0:
		dum = n/2
		count += 1
		return update(dum, count)
	elif n == 1:
		return count
	else:
		dum = n*3 + 1
		count += 1
		return update(dum, count)

def collatz(n):
	h.write(str(n) + ":" + str(update(n, 0)) + ",")
	update(n, 0)
	
for i in range(1, 1000000):
	collatz(i)

print "Time: ", '%3d' %(time() - start), "seconds"