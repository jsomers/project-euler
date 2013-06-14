# How many continued fractions for N <= 10000 have an odd period?
from math import floor, sqrt, ceil
from time import time
start = time()
def is_square(n):
	if ceil(pow(n, 1./2))**2 == n:
		return True
	else:
		return False

def cont_frac(n, a, b, c, ct, L, oa, ob, oc):
	if a == oa and b == ob and c == oc and ct > 1:
		return len(L) + 1
	if ct > 1:
		L.append(a)
	new_a = floor((b*(floor(sqrt(n)) + c))/(n-c**2))
	new_b = (n - c**2)/b
	new_c = abs(c - (new_a*(n - c**2)/b))
	return cont_frac(n, new_a, new_b, new_c, ct+1, L, oa, ob, oc)

ct = 0
for i in range(2, 10001):
	if is_square(i) == False:
		if cont_frac(i, floor(sqrt(i)), 1, floor(sqrt(i)), 0, [], floor((1*(floor(sqrt(i)) + floor(sqrt(i))))/(i-floor(sqrt(i))**2)), (i - floor(sqrt(i))**2)/1, abs(floor(sqrt(i)) - (floor((1*(floor(sqrt(i)) + floor(sqrt(i))))/(i-floor(sqrt(i))**2))*(i - floor(sqrt(i))**2)/1))) %2. != 0:
			ct+=1

print ct, time() - start, 'seconds'