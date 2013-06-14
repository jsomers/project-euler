# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.

from random import randint

# possible triplets: choose A, B, C s.t. C > A ^ B and A + B > C.

raw = open('/raw.txt', 'r')

triplets = []

for line in raw:
	raw_string = str(line)
	new_string = raw_string.replace("\n", "")
	triplets.append(new_string)

tru = []

for i in range(len(triplets)):
	v = triplets[i]
	v.rstrip()
	n = v.split(',')
	for i in range(len(n)):
		n[i] = int(n[i])
	tru.append(n)

for i in range(len(tru)):
	val = tru[i]
	A = val[0]
	B = val[1]
	C = val[2]
	if A**2 + B**2 == C**2:
		print A, B, C
		
# try 3,4,5; 5,12,13; 8,15,17; 7,24,25; 15,112,113

# from random import randint
# h = open('/nice.txt', 'w')
# 	for a in range(0, 1000, 3):
# 		for b in range(0, 1000, 4):
# 			for c in range(0, 1000, 5):
# 				if a**2 + b**2 == c**2 and a + b + c == 1000:
# 					h.write(str(a) + ", " + str(b) + ", " + str(c) + " sum: " + str(a + b + c) + "\n")