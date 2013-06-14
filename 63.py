# How many n-digit positive integers exist which are also an nth power?
things = []
for n in range(22):
	for i in range(100):
		if len(str(i**n)) > n:
			break
		if len(str(i**n)) == n:
			things.append(i**n)

print len(things) - 1 # don't count zero