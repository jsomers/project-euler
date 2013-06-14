# What is the maximum 16-digit string for a "magic" 5-gon ring?
a = 6
b = 5
c = 3

for d in range(10, 0, -1):
	for e in range(10, 0, -1):
		for f in range(10, 0, -1):
			for g in range(10, 0, -1):
				for h in range(10, 0, -1):
					for i in range(10, 0, -1):
						for j in range(10, 0, -1):
							if d + c + e == 14 and f + e + h == 14 and g + h + i == 14 and j + i + b == 14 and len(set([a, b, c, d, e, f, g, h, i, j])) == 10:
								print str(a) + str(b) + str(c) + str(d) + str(c) + str(e) + str(f) + str(e) + str(h) + str(g) + str(h) + str(i) + str(j) + str(i) + str(b)