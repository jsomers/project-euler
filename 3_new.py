big = 600851475143
x = 2

while big > 1:
	if big % x == 0:
		big = big / x
	else:
		x += 1

print x