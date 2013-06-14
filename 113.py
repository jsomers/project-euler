from time import time
start = time()
def genius(L, period, tots, diff):
	if period == 1:
		L = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
		diff = 1
	if period == 2:
		L = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
	if period >= 2:
		tots.append(L[0])
#	print 'the number of increasing numbers below', 10**(period-1), '(' + str(period-1) + ' zeroes)', 'is', L[0]
#	print 'the number of decreasing numbers below', 10**(period-1), '(' + str(period-1) + ' zeroes)', 'is', sum(tots) - (len(tots)-1)
	diff += 9
	if period == 101:
		print 'answer: ', str(period-1), sum(tots) - (len(tots)-1) + L[0] - diff - 1, time() - start, 'seconds'
		return
	for i in range(10):
		L[i] = sum(L) - sum(L[:i])
	return genius(L, period+1, tots, diff)

genius([], 1, [], 0)

'''
def dec(n):
	l = list(str(n))
	ct = 0
	for i in range(len(l)):
		if i+1 >= len(l):
			if ct > 0:
				return False
			if ct == 0:
				return True
		if l[i] < l[i+1]:
			ct+=1
			return False
	return True

def inc(n):
	l = list(str(n))
	ct = 0
	for i in range(len(l)):
		if i+1 >= len(l):
			if ct > 0:
				return False
			if ct == 0:
				return True
		if l[i] > l[i+1]:
			ct+=1
			return False
	return True
	
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

decs = []
bouncies = []
incs = []
for i in range(10000):
	if inc(i) == True:
		incs.append(i)
	if dec(i) == True:
		decs.append(i)
	if bouncy(i) == True:
		bouncies.append(i)

print 'increasing:', len(incs), 'decreasing:', len(decs), 'bouncies:', len(bouncies), 'non-bouncies:', 10000 - len(bouncies), 'salient:', (10000 - len(bouncies)) - (len(incs) + len(decs))
# 1 10 19 28 10000: 37, 46, 55, 64, 73, 82
'''