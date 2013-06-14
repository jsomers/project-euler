# Discover all the fractions with an unorthodox cancelling method.

for a in range(1, 10):
	for b in range(1, 10):
		for c in range(1, 10):
			for d in range(1, 10):
				if (10.*a + b)/(10.*c + d) == float(a)/d and int(str(a) + str(b)) < int(str(c) + str(d)):
					print str(a) + str(b) + '/' + str(c) + str(d)

print str(49*19*16*26) + '/' + str(98*95*64*65)