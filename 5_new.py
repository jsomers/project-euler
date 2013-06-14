# What is the smallest number that is evenly divisible by all the numbers from 1 to 20?
# 232792560

# We don't need this function!
def candidate(n):
	"""Checks whether n is divisible by 1-20 """
	return [n % x for x in range(1, 21)] == [0]*20

print (2 ** 4) * (3 ** 2) * 5 * 7 * 11 * 13 * 17 * 19