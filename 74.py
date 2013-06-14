# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
# 974322 (6! - 14*4!) and 1479 (4!) and 4079 (4! - 3!) + 6! - 4!
'''
22****
2*2***
2**2**
2***2*
2****2
etc.
'''
def mul(a, b):
	return a*b
	
def fact(n):
	facts = [1]
	for i in range (1, n+1):
		facts.append(i)
	return reduce(mul, facts)
	
def fact_digits(n):
	tot = 0
	digits = [int(d) for d in list(str(n))]
	for x in digits:
		tot += fact(x)
	return tot

def loop(found, n, count):
	a = fact_digits(n)
	if a not in found:
		found.append(a)
		return loop(found, a, count+1)
	else:
		return count+1, found

def do(n):
	return loop([n], n, 0)

print fact(6) + fact(4) - fact(3) - 14*fact(4)
'''
# Find them this way (and using range(1000000, 900000, -1))
ct = 0
for i in range(0, 10000, -1):
	if do(i)[0] == 60:
		ct += 1
		print i, ct
'''