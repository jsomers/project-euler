def triangle(n):
	return sum(range(n, -1, -1))

for i in range(100):
	for j in range(100):
		if (abs(triangle(i) * triangle(j) - 2*(10**6))) < 1000:
			print i, j, triangle(i) * triangle(j), i*j