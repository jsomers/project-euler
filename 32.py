# find the sum of all the pandigital products

# 1 x 4 = 4
# 4 x 1 = 4
# 2 x 3 = 4
# 3 x 2 = 4

def checker(s):
	if s.count('1') == 1 and s.count('2') == 1 and s.count('3') == 1 and s.count('4') == 1 and s.count('5') == 1 and s.count('6') == 1 and s.count('7') == 1 and s.count('8') == 1 and s.count('9') == 1:
		return True
	else:
		return False
		
matches = []
for i in range(1, 10): # 1-digit
	for j in range(1000, 10000): # 3-digit
		if i * j > 1000 and i * j < 10000 and checker(str(i) + str(j) + str(i*j)) == True:
			print i, j, i*j
			matches.append(i*j)

for i in range(10, 101): # 2-digit
	for j in range(1, 10000):
		if i * j > 1000 and i * j < 10000 and checker(str(i) + str(j) + str(i*j)) == True:
			print i, j, i*j
			matches.append(i*j)

print matches
print sum(matches) - 5796 - 5346 # remove duplicates