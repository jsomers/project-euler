# Give the sum of the digits in 100!

def mul(x, y):
	return x*y
def fact(n):
	facts = []
	for i in range (1, n+1):
		facts.append(i)
	a = reduce(mul, facts)
	return a

print fact(100)

string = '93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000'

numbers = []

for l in string:
	numbers.append(int(l))

print sum(numbers)