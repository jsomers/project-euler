from math import floor
from time import time

def sum(L):
	return reduce(lambda x, y: x + y, L)

def product(L):
	return reduce(lambda x, y: x * y, L)
	
def a(L):
	s = sum(L)
	p = product(L)
	return int(L[0] + floor(L[0] * (s - p) / p) + 1)

def t(L):
	s = sum(L)
	p = product(L)
	if s < p:
		return 0
	elif s > p:
		return 1
	elif s == p:
		return 2

def next(L, i):
	for index in range(len(L[:i]) + 1):
		L[index] = L[i] + 1
	return L

def format(L):
	i = 0
	report = []
	while L[i] > 1:
		report.append(L[i])
		i += 1
	report.append(str(len(L) - i) + ' x1')
	report.insert(0, sum(L))
	return report

def run(n):
	start = time()
	it = [2, 2] + [1] * (n - 2)
	print it
	i = 1
	sols = []
	while i <= 8:
		test = t(it)
		if test == 1:
			it[0] = a(it)
			i = 1
		elif test == 2:
			sols.append(format(it))
			it[0] = a(it)
			i = 1
		elif test == 0:
			new = next(it, i)
			it = new[::]
			i += 1
	sols.sort()
 	return sols[0][0], time() - start #CHANGE

f = open('/marmet_results.txt', 'a')

for i in range(11762, 11506, -1):
	f.write(str(i) + str(run(i)) + '\n')