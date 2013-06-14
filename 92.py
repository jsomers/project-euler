# A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before... How many starting numbers below ten million will arrive at 89?
# something fishy here
from time import time
start = time()
def ss_dig(n):
	tot = 0
	for x in list(str(n)):
		tot += int(x)**2
	return tot

mat = [0]*569

for x in range(1, 568):
	n = x
	while x != 89 and x != 1:
		x = ss_dig(x)
		if x == 89:
			mat[n] = 1

ct = 0
for n in range(1, 10000001):
	if mat[ss_dig(n)] == 1:
		ct += 1
	else:
		pass

print ct, time() - start