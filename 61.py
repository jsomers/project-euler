# Find the sum of the only set of six 4-digit figurate numbers with a cyclic property.

def last_two(n):
	return int("".join(map(str, list(str(n))[2:])))

def first_two(n):
	return int("".join(map(str, list(str(n))[:2])))
	
tri = [n*(n+1)/2 for n in range(160) if n*(n+1)/2 > 1000 and n*(n+1)/2 < 10000 and last_two(n*(n+1)/2) > 9]
squ = [n**2 for n in range(100) if n**2 > 1000 and n**2 < 10000 and last_two(n**2) > 9]
pen = [n*(3*n-1)/2 for n in range(160) if n*(3*n-1)/2 > 1000 and n*(3*n-1)/2 < 10000 and last_two(n*(3*n-1)/2) > 9]
sex = [n*(2*n-1) for n in range(180) if n*(2*n-1) > 1000 and n*(2*n-1) < 10000 and last_two(n*(2*n-1)) > 9]
hep = [n*(5*n-3)/2 for n in range(160) if n*(5*n-3)/2 > 1000 and n*(5*n-3)/2 < 10000 and last_two(n*(5*n-3)/2) > 9]
och = [n*(3*n-2) for n in range(160) if n*(3*n-2) > 1000 and n*(3*n-2) < 10000 and last_two(n*(3*n-2)) > 9]
ALL = [tri, squ, pen, sex, hep, och]


def stage1(n, firstlist):
	availables = [i for i in range(6) if i != ALL.index(firstlist)]
	for a in availables:
		for match in ALL[a]:
			if last_two(n) == first_two(match):
				pair = [n, match]
				newL = [i for i in range(6) if i in availables and i != a]
				stage2(pair, newL)

def stage2(pair, availables):
	for a in availables:
		for match in ALL[a]:
			if last_two(pair[1]) == first_two(match):
				trip = [pair[0], pair[1], match]
				newL = [i for i in range(6) if i in availables and i != a]
				stage3(trip, newL)

def stage3(trip, availables):
	for a in availables:
		for match in ALL[a]:
			if last_two(trip[2]) == first_two(match):
				quad = [trip[0], trip[1], trip[2], match]
				newL = [i for i in range(6) if i in availables and i != a]
				stage4(quad, newL)

def stage4(quad, availables):
	for a in availables:
		for match in ALL[a]:
			if last_two(quad[3]) == first_two(match):
				quint = [quad[0], quad[1], quad[2], quad[3], match]
				newL = [i for i in range(6) if i in availables and i != a]
				stage5(quint, newL)

def stage5(quint, availables):
	for a in availables:
		for match in ALL[a]:
			if last_two(quint[4]) == first_two(match) and last_two(match) == first_two(quint[0]):
				finish = [quint[0], quint[1], quint[2], quint[3], quint[4], match]
				print finish, sum(finish)
for i in pen:
	stage1(i, pen)