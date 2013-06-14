# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

from math import ceil
# na + b + n^2

# b must be prime
# a must be odd
# a, b < 1000

Bs = [17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 83, 89, 97, 101, 107, 113, 127, 131, 149, 151, 173, 197, 199, 223, 227, 251, 257, 281, 313, 347, 383, 421, 461, 503, 547, 593, 641, 647, 691, 743, 797, 853, 911, 971]
As = range(-63, 49, 2)

def half(n):
	return int(ceil(n/2)+1)
	
def prime(n):
	ct = 0
	for i in range(1, half(n)):
		x = float(n)/i
		if x % 1 == 0:
			ct += 1
	if ct == 1:
		return True
	else:
		return False

def tester(a, b):
	ct = 0
	for i in range(100):
		if prime(i*a + b + i**2) == False:
			print i
			return

# test to see if 20a + b + 400 is prime
for b in Bs:
	for a in As:
		if prime(a + b + 1) == True and prime(2*a + b + 4) == True and prime(3*a + b + 9) == True and prime(4*a + b + 16) == True and prime(5*a + b + 25) == True and prime(6*a + b + 36) == True and prime(7*a + b + 49) == True and prime(8*a + b + 64) == True and prime(9*a + b + 81) == True and prime(10*a + b + 100) == True and prime(11*a + b + 121) == True and prime(12*a + b + 144) == True and prime(13*a + b + 169) == True and prime(14*a + b + 196) == True and prime(15*a + b + 225) == True and prime(16*a + b + 256) == True and prime(17*a + b + 289) == True and prime(18*a + b + 324) == True and prime(19*a + b + 361) == True and prime(20*a + b + 400) == True and prime(21*a + b + 441) == True and prime(22*a + b + 484) == True and prime(23*a + b + 529) == True and prime(24*a + b + 576) == True and prime(25*a + b + 625) == True:
				print a, b
				tester(a, b)
tester(-1, 41)

# -61 971