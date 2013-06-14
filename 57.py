# Investigate the expansion of the continued fraction for the square root of two.

def num(n):
	c = 0
	if n == 1:
		return 3
	if n == 2:
		return 7
	a = 3
	b = 7
	ct = 0
	while ct < n-2:
		c = 2*b + a
		a = b
		b = c
		ct += 1
	return c

def den(n):
	c = 0
	if n == 1:
		return 2
	if n == 2:
		return 5
	a = 2
	b = 5
	ct = 0
	while ct < n-2:
		c = 2*b + a
		a = b
		b = c
		ct += 1
	return c

def digits(n):
	a = n
	ct = 0
	while a > 1:
		a = a/10
		ct += 1
	return ct+1

ct = 0
for i in range(1001):
	if digits(num(i)) > digits(den(i)):
		ct+=1

print ct
