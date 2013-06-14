from time import time
start = time()
def bouncy(n):
	neg, pos = 0, 0
	l = list(str(n))
	for i in range(len(l)):
		if i+1 >= len(l):
			if pos > 0 and neg > 0:
				return True
			else:
				return False
		if l[i+1] > l[i]:
			pos+=1
		if l[i+1] < l[i]:
			neg+=1
	if neg > 0 and pos > 0:
		return True
	else:
		return False

n = 2000000
b = 0
for i in range(1, n + 1):
	if bouncy(i) == True:
		b += 1
	if float(b)/i == .99:
		print i, time() - start