from time import time
from math import ceil

start = time()

def half(n):
	return int(ceil(n/2 + 1))
	
def divisors(n):
	div_sum = 0
	divisor_count = 0
	for i in range(1, half(n)):
		if (float(n)/i) % 1 == 0:
			div_sum += i
	return div_sum

pairsum = 0

for a in range(2, 10000, 2):
	b = divisors(a)
	t = divisors(b)
	if a == t and a != b:
		print a, "and", b, "are an amicable pair"
		pairsum += a + b

print str(pairsum/2)

print "Time: ", '%3d' %(time() - start), "seconds"