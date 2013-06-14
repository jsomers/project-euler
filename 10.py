# Find the sum of all the primes below one million.
# What is the 10001st prime number?

from math import sqrt
from time import time, struct_time

start = time()
h = open('/known_primes.txt', 'r')
numbers = []
for line in h:
	raw_string = str(line)
	new_string = raw_string.replace("\n", "")
	numbers.append(int(new_string))
print sum(numbers)

print time() - time

# s = range(1, 1000000)

# for i in range(len(s)):
#	x = s[i]
#	for j in range(2, 1000):
#		if x % j == 0 and x != j:
#			s[i] = ""
#	h.write(str(s[i]) + "\n")
