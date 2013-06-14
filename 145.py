from time import time

start = time()

def all_odd(n):
	for i in range(len(str(n))):
		if n // 10**i % 2. == 0:
			return 0
	return 1

def is_reversible(n):
	if (n % 10.) % 2. == (n // 10**(len(str(n)) - 1)) % 2.:
		return 0
	if n % 10. == 0:
		return 0	
	return all_odd(n + int(str(n)[::-1]))

# 10^1 # 8 + 6 + 4 + 2 = 20
# 10^2 # 10 + 20 + 30 + 40 = 100
# 10^3 # 240 + 180 + 120 + 60 = 600 = 20 * 30
# 10^4 # 0 + 0 + 0 + 0 = 0
# 10^5 # 7,200 + 5,400 + 3,600 + 1,800 = 18,000 = 600 * 30
# 10^6 # 5,000 + 10,000 + 15,000 + 20,000 = 50,000
# 10^7 # 216,000 + 162,000 + 108,000 + 54,000 = 540,000 = 18,000 * 30
# 10^8 # 0 + 0 + 0 + 0
print 20 + 100 + 600 + 18000 + 50000 + 540000 + 0
tot = 0
for i in range(1 * 10**1, 2 * 10**2 + 1, 2):
	tot += is_reversible(i)

print tot * 2, time() - start