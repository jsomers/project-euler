# Find the smallest member of the longest amicable chain with no element 
# exceeding one million.
from time import time
from egypt import *

def pds(n):
	return list(divisors(n))[:-1]

def chain(a):
	n = a
	i = 1
	L = [a]
	while n < 10 ** 6:
		n = sum(pds(n))
		L.append(n)
		if i > 1 and n in L[1:-1]: # hit a loop
			return None
		if n == 0: # hit a prime
			return None
		if n == a: # actually got back to self
			return L[:-1]
		i += 1
"""
start = time()
chains = []
for i in range(1, 10 ** 6):
	ch = chain(i)
	if ch:
		chains.append((len(ch), i))
	if i % 10 ** 3 == 0:
		print str(i / 10. ** 4) + '%', time() - start

chains.sort()
print chains[::-1]"""

f = open('candidates.txt', 'rU').read()

strs = [a.strip().replace('[', '').replace(']', '') for a in f.split('),')]
strs2 = [a.replace('(', '').replace(')', '') for a in strs]
candidates = [[int(i.replace(',', '')) for i in a.split()] for a in strs2]

for ca in candidates:
	ch = chain(ca[1])
	if max(ch) < 10 ** 6:
		print min(ch)
		break