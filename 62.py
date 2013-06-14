# Find the smallest cube for which exactly five permutations of its digits are cube.
from math import ceil
def is_cube(n):
	if ceil(pow(n, 1./3))**3 == n:
		return True
	else:
		return False

def has_permutations(n, L):
	hitters = []
	for item in L:
		if len(str(item)) == len(str(n)):
			hits = 0
			for i in range(0, 10):
#				print i, item, n, str(item).count(str(i)), str(n).count(str(i))
				if str(n).count(str(i)) == str(item).count(str(i)) and str(n).count(str(i)) > 0:
					hits += str(n).count(str(i))
				else:
					pass
			if hits == len(str(n)):
				hitters.append(item)
			else:
				pass
	return hitters

def sum_digits(n):
	a = 0
	for e in list(str(n)):
		a += int(e)
	return a

cubes = [i**3 for i in range(4650, 11000)] # 11-digits

'''
for i in cubes:
	L = list(str(i))
	L.sort()
	cubes[cubes.index(i)] = int("".join(map(str, L)))

print cubes
'''
def to_ten(n):
	ten = 0
	for i in range(10):
		ten += str(n).count(str(i)) * 10**i
	return ten
specials = []
for i in cubes:
	specials.append((to_ten(i), i))

specials.sort()

ct = 0
for i in range(len(specials)-1):
	if specials[i][0] == specials[i+1][0]:
		ct+=1
	if specials[i][0] != specials[i+1][0]:
		ct = 0
	if ct > 3:
		print specials[i-3][1]
'''
for i in cubes:
	if len(has_permutations(i, cubes)) >= 3:
		print i, has_permutations(i, cubes)
'''