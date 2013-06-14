# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits in some order.
from math import ceil

def to_ten(n):
	ten = 0
	for i in range(10):
		ten += str(n).count(str(i)) * 10**i
	return ten

for i in range(100000, int(ceil(1000000/6))):
	hits = 0
	for j in range(2, 7):
		if to_ten(i*j) == to_ten(i):
			hits += 1
	if hits == 5:
		print i, 'success' 