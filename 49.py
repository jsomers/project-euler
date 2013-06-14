# Find arithmetic sequences, made of prime terms, whose four digits are permutations of each other.

from time import time
start = time()

def has_permutations(n, L):
	hitters = []
	for item in L:
		hits = 0
		for i in range(0, 10):
			# print i, item, n, str(item).count(str(i)), str(n).count(str(i))
			if str(n).count(str(i)) == str(item).count(str(i)) and str(n).count(str(i)) > 0:
				hits += str(n).count(str(i))
			else:
				pass
		if hits == 4:
			hitters.append(item)
		else:
			pass
	return hitters

def contains_seq(L):
	L.sort()
	ct = 0
	for a in L:
		for b in L[L.index(a):]:
			for c in L[L.index(b):]:
				if c - b == b - a and b - a != 0:
					print a, b, c
					ct += 1
				else:
					pass
	if ct > 0:
		return True
	else:
		return False

h = open('/Users/jsomers/Desktop/Work/Project Euler/primes.txt', 'r')

primes = []
for line in h:
	raw_string = str(line)
	new_string = raw_string.replace("\n", "")
	primes.append(int(new_string))

print primes[168], has_permutations(primes[168], primes[168:1230])

for j in range(168, 1230):
#	print j, primes[j], has_permutations(primes[j], primes[168:1230])
	if contains_seq(has_permutations(primes[j], primes[168:1230])) == True: # slice for four-digit primes
		print has_permutations(primes[j], primes[168:1230])

print time() - start, 'seconds'
