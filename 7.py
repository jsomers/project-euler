# What is the 10001st prime number?
from math import sqrt

h = open('/known_primes.txt', 'w')

s = range(150000)

for i in range(len(s)):
	x = s[i]
	for j in range(2, 390):
		if x % j == 0 and x != j:
			s[i] = ""
	h.write(str(s[i]) + "\n")
		