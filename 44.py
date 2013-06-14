# Find the smallest pair of pentagonal numbers whose sum and difference is pentagonal.

from math import sqrt

def abs(n):
	if n < 0:
		return -n
	else:
		return n

def pent(n):
	return n*(3*n-1)/2

pentagonals = []
for i in range(1, 7000):
	pentagonals.append(pent(i))

def check(i): # much faster than looking through pentagonals every time
	if (1 + sqrt(1 + 24*i))/6 % 1. == 0:
		return True
	else:
		return False

for i in pentagonals:
	for j in pentagonals:
		if check(i+j) == True and check(abs(i-j)) == True:
			print i, j