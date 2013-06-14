# http://projecteuler.net/index.php?section=problems&id=108
from time import time
start = time()
d = {}

# Build dictionary of denominators.
for n in range(1, 100000):
	d.setdefault((1. / n), 0)

for x in range(1, 5000):
	for y in range(x, 5000):
		try:
			d[(1. / x) + (1. / y)] += 1
		except:
			pass

print max(d.values()), time() - start