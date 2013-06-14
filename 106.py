# Wow!

def fact(n):
	"factorial"
	return reduce(lambda x, y: x * y, range(1, n + 1))

def nCr(n, r):
	"n choose r"
	if n == r:
		return 1
	else:
		return fact(n) / (fact(r) * fact(n - r))

def x_with_x(n, x):
	"number of *disjoint* x-subset pairs one can form with an array of length n"
	if n - x >= x:
		return (nCr(n, x) * nCr(n - x, x)) / 2
	else:
		return 0

catalans = {2:2, 3:5, 4:14, 5:42, 6:132}

def dominated(n, x):
	"number of 'strictly dominated' x_with_x guys -- these need not be checked"
	return nCr(n, 2 * x) * catalans[x]

def need_to_check(n):
	"number of disjoint subset pairs we need to check for array length n"
	tot = 0
	for x in range(2, n // 2 + 1):
		tot += x_with_x(n, x) - dominated(n, x)
	return tot

print need_to_check(12)