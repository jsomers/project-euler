# Start with "near optimum set"
# Make sure sums of all 2 ** 7 subsets are unique
# Try breaking the size rules: compare largest 3-set to smallest 4-set, etc.
# Change the set in some smart way (or, explore the space randomly)

from random import randint

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

nos1 = [19, 30, 37, 38, 39, 41, 44]
nos2 = [20, 31, 38, 39, 40, 42, 45] # This is the answer!

while True:
	test = [a + randint(-3, 3) for a in nos1]
	
	subsets = [list(A) for A in list(powerset(test))]
	subset_sums = [sum(a) for a in subsets]

	#print sorted(subset_sums)
	#print sorted(zip(subset_sums, subsets))

	#print ''.join([str(a) for a in test]), sum(test)

	#print len(set(subset_sums)), len(subset_sums), 

	three_sets = [a for a in subsets if len(a) == 3]
	four_sets = [a for a in subsets if len(a) == 4]
	three_set_sums = [sum(a) for a in three_sets]
	four_set_sums = [sum(a) for a in four_sets]

	#print min(four_set_sums), max(three_set_sums), 
	if len(set(subset_sums)) == len(subset_sums) and min(four_set_sums) > max(three_set_sums):
		print test, sum(test)
		break