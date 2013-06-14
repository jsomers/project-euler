def checker(s):
	if s.count('1') == 1 and s.count('2') == 1 and s.count('3') == 1 and s.count('4') == 1 and s.count('5') == 1 and s.count('6') == 1 and s.count('7') == 1:
		return True
	else:
		return False

h = open('/07368791.txt', 'r')

primes = []
for line in h:
	raw_string = str(line)
	new_string = raw_string.replace("\n", "")
	primes.append(int(new_string))

for n in primes:
	if checker(str(n)) == True:
		print n