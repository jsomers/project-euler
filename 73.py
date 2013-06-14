# How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d <= 10,000?

from math import ceil, floor
from time import time

Start = time()

Low = 1./3; High = 1./2

def bounds(den):
	""" Limits numerator search space """ 
	return int(floor(den/3.)), int(ceil(den/2.))

found = []
for d in xrange(1, 10001):
	for n in range(bounds(d)[0], bounds(d)[1] + 1):
		decimal = float(n)/d
		if decimal > Low and decimal < High:
			found.append(decimal)

print len(set(found)), time() - Start