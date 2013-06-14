# How many values of C(n,r), for 1 <= n <= 100, exceed one-million?

from time import time
start = time()
def mul(x, y):
	return x*y
	
def fact(n):
	facts = [1]
	for i in range (1, n+1):
		facts.append(i)
	return reduce(mul, facts)

def Choose(n, r):
	return reduce(mul, range( n-r + 1, n+1))/fact(r)

print Choose(5, 3)
ct = 0
for n in range(1, 101):
	for r in range(1, n+1):
		C = Choose(n, r)
		if C > 1000000:
			ct += 1
	print n, ct, time() - start, 'seconds'