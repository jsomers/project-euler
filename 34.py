# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

def mul(x, y):
	return x*y
	
def fact(n):
	facts = [1]
	for i in range (1, n+1):
		facts.append(i)
	a = reduce(mul, facts)
	return a

def fact_digits(n):
	tot = 0
	digits = list(str(n))
	for n in digits:
		tot += fact(int(n))
	return tot

results = []
for i in range(1, 100000):
	if i == fact_digits(i):
		results.append(i)

print sum(results) - 3 # exclude 1! and 2!