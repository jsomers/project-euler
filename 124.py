from totient import *

def mul(x, y):
	return x*y
	
def rad(n):
	t = []
	for factor in factors(n):
		t.append(factor[0])
	return reduce(mul, t)

rads = []
for n in range(2, 100001):
	rads.append((rad(n), n))

rads.insert(0, (1, 1))
rads.sort()
print rads[9999][1]