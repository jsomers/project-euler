# Find the smallest odd composite that cannot be expressed as the sum of a prime and two times a square

from math import ceil, sqrt

h = open('/primes.txt', 'r')
primes = []
for line in h:
	raw_string = str(line)
	new_string = raw_string.replace("\n", "")
	primes.append(int(new_string))

for A in range(1, 100001, 2):
	for p in primes:
		if p > A:
			print A, 'success'
			break
		if sqrt((A-p)/2) % 1. == 0:
			break
		else:
			pass