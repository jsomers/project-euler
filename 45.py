# After 40755, what is the next triangle number that is also pentagonal and hexagonal?

from math import sqrt

def is_pent(i):
	if (1 + sqrt(1 + 24*i))/6 % 1. == 0:
		return True
	else:
		return False

def is_hex(i):
	if (1 + sqrt(1 + 8*i))/4 % 1. == 0:
		return True
	else:
		return False

def tri(i):
	return i*(i+1)/2

triangles = []
for i in range(100000):
	triangles.append(tri(i))

for tri in triangles:
	if is_pent(tri) == True and is_hex(tri) == True:
		print tri