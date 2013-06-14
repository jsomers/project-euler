# Find the largest prime factor of 317584931803.

# Need primality test
# Need to factor (go backwards)

# Divide by 2, then 3, then 4, etc... get x
# Is x an integer?
# If so, is x prime?

start = 317584931803./2 + 1.5
factors = []
for i in range(1, 5717821):
	x = 317584931803./i
	if x % 1 == 0 and x < 317584931803:
		print x, "i =", i
		factors.append(i)
		for j in range(2, 10000):
			y = x/j
			if y % 1 == 0:
				print j
				break

print factors

# primality tester
for j in range(2, 10000):
	y = 3248851./j
	if y % 1 == 0:
		print j
		break