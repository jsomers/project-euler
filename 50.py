# Which prime, below one-million, can be written as the sum of the most consecutive primes?
from time import time
start = time()
h = open('/primes.txt', 'r')
primes = []

for line in h:
	raw_string = str(line)
	new_string = raw_string.replace("\n", "")
	primes.append(int(new_string))

for i in range(1000, 0, -1):
	for j in range(0, 78499 - i):
		t = sum(primes[j:i+j]) # from 0 to 1000, 1 to 1001, 2 to 1002
		if sum(primes[j:i+j]) > 1000000:
			break
		elif sum(primes[j:i+j]) in primes:
			print i, sum(primes[j:i+j]), time()-start, 'seconds'