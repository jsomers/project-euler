from math import ceil
from time import time
start = time()

def is_square(n):
	if ceil(pow(n, .5))**2 == n:
		return 1
	else:
		return 0
counts = []
for M in range(100, 105):
	integer_count = 0
	false_positives = 0
	for i in range(1, M+1):
		for j in range(i, M+1):
			for k in range(j, M+1):
				one = float(j)**2. + (float(i)+k)**2.
				two = float(k)**2. + (float(i)+j)**2.
				three = float(i)**2. + (float(j)+k)**2.
				Min = min([one, two, three])
				if is_square(one) == 1 and one != Min:
					false_positives += 1
				elif is_square(two) == 1 and two != Min:
					false_positives += 1
				elif is_square(three) == 1 and three != Min:
					false_positives += 1
				if is_square(Min) == 1:
					integer_count += 1

	counts.append(false_positives)
print counts

the_list = [0, 0, 0, 0, 0, 0, 1, 3, 4, 6, 9, 12, 15, 19, 23, 26, 29, 33, 39, 46, 53, 60, 68, 76, 83, 92, 101, 110, 119, 129, 140, 152, 164, 177, 192, 207, 222, 238, 254, 271, 289, 309, 330, 352, 373, 391, 411, 431, 450, 472, 495, 518, 541, 565, 590, 615, 639, 665, 692, 720, 747, 777, 808, 838, 867, 898, 931, 966, 1000, 1034, 1070, 1106, 1142, 1180, 1218, 1254, 1291, 1328, 1366, 1405, 1443, 1483, 1524, 1566, 1607, 1650, 1694, 1738, 1783, 1831, 1879, 1928, 1976, 2024, 2074, 2125, 2176, 2230, 2285, 2340]