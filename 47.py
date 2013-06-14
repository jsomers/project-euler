# What are the first four consecutive numbers to have four distinct prime factors?

''' First result is a false positive, not sure why '''

from time import time
from math import ceil, sqrt

start = time()

h = open('/primes.txt', 'r')
primes = []
for line in h:
	raw_string = str(line)
	new_string = raw_string.replace("\n", "")
	primes.append(int(new_string))
	
def distinct_prime_factors(n):
	ct=0
	for i in primes[:200]:
		if (n/float(i)) % 1. == 0:
			ct += 1
	return ct

ct = 0

for i in range(0, 500000):
	if ct == 4:
		print i-4, "found in", time() - start, "seconds"
	if distinct_prime_factors(i) != 4:
		if ct > 0:
			ct -= 1
	else:
		ct += 1

print time() - start, 'seconds'