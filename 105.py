from math import ceil

def powerset(s):
    d = dict(zip(
            (1<<i for i in range(len(s))),
            (set([e]) for e in s)
            ))

    subset = set()
    yield subset
    for i in range(1, 1<<len(s)):
        subset = subset ^ d[i & -i]
        yield subset

def test1(s):
	subsets = [list(A) for A in list(powerset(s))]
	subset_sums = [sum(a) for a in subsets]
	return len(set(subset_sums)) == len(subset_sums)

def test2(s):
	s.sort()
	l = len(s)
	if l % 2 == 0:
		i = l / 2 + 1
	else:
		i = int(ceil(l / 2.))
	
	min_maxes = [0] * l
	subsets = [list(A) for A in list(powerset(s))]
	for i in range(1, l):
		i_sub_sums = [sum(a) for a in subsets if len(a) == i]
		min_maxes[i] = (min(i_sub_sums), max(i_sub_sums))
	for i in range(1, l - 1):
		if min_maxes[i][1] > min_maxes[i + 1][0]:
			return False
	return True

def test(s):
	return test1(s) and test2(s)


lines = open('sets.txt', 'rU').readlines()

sets = [a.split(',') for a in lines]
sets = [[int(a) for a in s] for s in sets]

specials = []

for s in sets:
	if test(s):
		print s, sum(s)
		specials.append(sum(s))

print sum(specials)