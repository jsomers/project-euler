# By listing the set of reduced proper fractions for d <= 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.
from math import floor
theNum = 3./7

rat = .42857

diffs = []
for d in xrange(1000000, 999990, -1):
	for n in xrange(int(floor(d*rat)), d):
		if float(n)/d < theNum and float(n+1)/d > theNum:
			print n, d, float(n)/d
			diffs.append((theNum - float(n)/d, n, d))

print min(diffs)