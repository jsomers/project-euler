# How many circular primes are there below one million?

'''This runs too slow'''
from time import time

start = time()

h = open('/primes.txt', 'r')

primes = []
for line in h:
	raw_string = str(line)
	new_string = raw_string.replace("\n", "")
	primes.append(int(new_string))

def rot_checker(n):
	if n > 100 and n < 1000: # 3-digits
		l = list(str(n))
		rot1 = int(str(l[1]) + str(l[2]) + str(l[0]))
		rot2 = int(str(l[2]) + str(l[0]) + str(l[1]))
		if rot1 in primes[25:168] and rot2 in primes[25:168]:
			return True
		else:
			return False
	if n > 1000 and n < 10000: # 4-digits
		l = list(str(n))
		rot1 = int(str(l[1]) + str(l[2]) + str(l[3]) + str(l[0]))
		rot2 = int(str(l[2]) + str(l[3]) + str(l[0]) + str(l[1]))
		rot3 = int(str(l[3]) + str(l[0]) + str(l[1]) + str(l[2]))
		if rot1 in primes[168:1230] and rot2 in primes[168:1230] and rot3 in primes[168:1230]:
			return True
		else:
			return False
	if n > 10000 and n < 100000: # 5-digits
		l = list(str(n))
		rot1 = int(str(l[1]) + str(l[2]) + str(l[3]) + str(l[4]) + str(l[0]))
		rot2 = int(str(l[2]) + str(l[3]) + str(l[4]) + str(l[0]) + str(l[1]))
		rot3 = int(str(l[3]) + str(l[4]) + str(l[0]) + str(l[1]) + str(l[2]))
		rot4 = int(str(l[4]) + str(l[0]) + str(l[1]) + str(l[2]) + str(l[3]))
		if rot1 in primes[1230:9593] and rot2 in primes[1230:9593] and rot3 in primes[1230:9593] and rot4 in primes[1230:9593]:
			return True
		else:
			return False
	if n > 100000 and n < 1000000: # 6-digits
		l = list(str(n))
		rot1 = int(str(l[1]) + str(l[2]) + str(l[3]) + str(l[4]) + str(l[5]) + str(l[0]))
		rot2 = int(str(l[2]) + str(l[3]) + str(l[4]) + str(l[5]) + str(l[0]) + str(l[1]))
		rot3 = int(str(l[3]) + str(l[4]) + str(l[5]) + str(l[0]) + str(l[1]) + str(l[2]))
		rot4 = int(str(l[4]) + str(l[5]) + str(l[0]) + str(l[1]) + str(l[2]) + str(l[3]))
		rot5 = int(str(l[5]) + str(l[0]) + str(l[1]) + str(l[2]) + str(l[3]) + str(l[4]))
		if rot1 in primes[9593:] and rot2 in primes[9593:] and rot3 in primes[9593:] and rot4 in primes[9593:] and rot5 in primes[9593:]:
			return True
		else:
			return False
	else:
		return

circles = []
for i in primes:
	if rot_checker(i) == True:
		circles.append(i)

print circles, str(len(circles) + 13)

print "Time: ", '%3d' %(time() - start), "seconds"