# http://projecteuler.net/index.php?section=problems&id=93

# Parentheses placements:
	# (1 + 2) + 3 + 4, ((1 2) 3) 4
	# 1 + 2 + (3 + 4), 1 + (2 + (3 + 4))
	# 1 + (2 + 3) + 4, (1 + (2 + 3)) + 4, 1 + ((2 + 3) + 4)
	# (1 + 2 + 3) + 4, 1 + (2 + 3 + 4)	
	# [0] 1 [1] + [2] 2 [3] + [4] 3 [5] + [6] 4 [7]

# Orderings:
	# 4! = 24

# Operations:
	# 4 ** 3 = 64

# All the sets:
	# 10 choose 6 = 210

# 2,903,040 total

from time import time
start = time()

S = (1, 2, 3, 4)

def parens(n):
	a = ('', '(', ')', '((', '))')
	return a[n]

def perms(s):
	perms = []
	for a in s:
		for b in s:
			if a != b:
				for c in s:
					if c != b and c != a:
						for d in s:
							if d != a and d != b and d != c:
								perms.append((float(a), float(b), float(c), float(d)))
	return perms

def all_ops(set_of_numbers):
	results = []
	ops = ('*', '+', '/', '-')
	pars = [(0, 0, 0, 0, 0, 0, 0, 0), (1, 0, 0, 2, 0, 0, 0, 0), (3, 0, 0, 2, 0, 2, 0, 0), (0, 0, 0, 0, 1, 0, 0, 2), (0, 0, 1, 0, 1, 0, 0, 4), (0, 0, 1, 0, 0, 2, 0, 0), (1, 0, 1, 0, 0, 4, 0, 0), (0, 0, 3, 0, 0, 2, 0, 2), (1, 0, 0, 0, 0, 2, 0, 0), (0, 0, 1, 0, 0, 0, 0, 2)]
	
	for s in perms(set_of_numbers):
		for par in pars:
			for op1 in ops:
				for op2 in ops:
					for op3 in ops:
						print (parens(par[0]) + str(float(s[0])) + parens(par[1]) + ' %s ' + parens(par[2]) + str(float(s[1])) + parens(par[3]) + ' %s ' + parens(par[4]) + str(float(s[2])) + parens(par[5]) + ' %s ' + parens(par[6]) + str(float(s[3])) + parens(par[7])) %(op1, op2, op3)
						try:
							results.append(eval((parens(par[0]) + str(float(s[0])) + parens(par[1]) + ' %s ' + parens(par[2]) + str(float(s[1])) + parens(par[3]) + ' %s ' + parens(par[4]) + str(float(s[2])) + parens(par[5]) + ' %s ' + parens(par[6]) + str(float(s[3])) + parens(par[7])) %(op1, op2, op3)))
						except:
							pass
							
	return set([int(abs(r)) for r in results if r % 1 == 0])

def combos():
	combos = []
	p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	for a in p:
		for b in p[a + 1:]:
			for c in p[b + 1:]:
				for d in p[c + 1:]:
					combos.append((a, b, c, d))
	return combos

for S in combos()[84:]:
	a = [i for i in all_ops(S)]
	if len(set(range(51)).difference(a)) == 0:
		print S, a, time() - start
		break