# Find the last ten digits of the series 1^1, 2^2, .... 1000^1000

total = 0

for i in range(1, 1001):
	total += i**i

print str(total)[len(str(total))-10:len(str(total))]