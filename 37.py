h = open('/known_primes.txt', 'r')

primes = []
for line in h:
	raw_string = str(line)
	new_string = raw_string.replace("\n", "")
	if new_string.count('2') == 0 and new_string.count('4') == 0 and new_string.count('6') == 0 and new_string.count('8') == 0 and new_string.count('0') == 0:
		primes.append(int(new_string))
		
# left
def l_trunc(n):
	ct = 0
	digits = list(str(n))
	length = len(digits)
	while length > 1:
		digits.pop(0)
		checkst = "".join(map(str, digits))
		check = int(checkst)
		if check not in primes:
			return False
			break
		else:
			ct += 1
		length -= 1
	if ct == len(list(str(n))) - 1 and len(list(str(n))) > 2:
		return True
	else:
		return False

# right
def r_trunc(n):
	ct = 0
	digits = list(str(n))
	length = len(digits)
	while length > 1:
		digits.pop()	# here
		checkst = "".join(map(str, digits))
		check = int(checkst)
		if check not in primes:
			return False
			break
		else:
			ct += 1
		length -= 1
	if ct == len(list(str(n))) - 1 and len(list(str(n))) > 2:
		return True
	else:
		return False

found = []
for i in primes:
	if l_trunc(i) == True and r_trunc(i) == True:
		found.append(i)
print found, sum(found) + 23 + 37 + 53 + 73