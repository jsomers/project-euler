# Which is the first triangle number to have over five-hundred divisors?
from time import time
from math import ceil
start = time()

def tri(n):
	return (n**2 + n)/2
		
def divisors(n):
	divisor_count = 0
	for i in range(1, n+1):
		if (float(n)/i) % 1 == 0:
			divisor_count += 1
	return divisor_count

for i in range(1, 15000, 2):
	if (divisors(i) * divisors(tri(i)/i)) > 300:
		print i, ":", tri(i), ":", divisors(i) * divisors(tri(i)/i)


print "Time: ", '%3d' %(time() - start), "seconds"