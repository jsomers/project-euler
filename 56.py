# What is the maximum digital sum for numbers a^b where a, b < 100?

def sum_digits(n):
	tot = 0
	for i in range(10):
		tot += i*str(n).count(str(i))
	return tot

sums = []
for a in range(100):
	for b in range(100):
		sums.append(sum_digits(a**b))

print max(sums)