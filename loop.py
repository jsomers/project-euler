# try 3,4,5; 5, 12, 13; 8, 15, 17; 7, 24, 25; 15, 112, 113

from random import randint
h = open('/nice.txt', 'w')
for a in range(0, 1000, 3):
	for b in range(0, 1000, 4):
		for c in range(0, 1000, 5):
			if a**2 + b**2 == c**2 and a + b + c == 1000:
				h.write(str(a) + ", " + str(b) + ", " + str(c) + " sum: " + str(a + b + c) + "\n")