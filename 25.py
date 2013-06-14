# Find the first Fib greater than 9*10^999 + 9*10^998 ... i.e., with 1,000 digits

fibs = []
p = 1
q = 1
a = 0

for i in range(4783):
	a = p+q
	thelist = list(str(a))
	if len(thelist) > 1000:
		print i - 2
		break
	p = q
	q = a