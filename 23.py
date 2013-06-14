# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
from math import ceil
from time import time
start = time()
''' Used to build the abundant numbers
def half(n):
	return int(ceil(n/2 + 1))

def divisors(n):
	div_sum = 0
	divisor_count = 0
	for i in range(1, half(n)):
		if (float(n)/i) % 1 == 0:
			div_sum += i
	return div_sum
'''
h = open('/abundants.txt', 'r')

for line in h:
	raw = str(line)
	abstrings = raw.split(',')

oabundants = []

for string in abstrings:
	num = int(string)
	oabundants.append(num)
abundants = []
for n in oabundants:
	if n < 22000:
		abundants.append(n)

odds = []
for i in abundants:
	if i % 2 != 0:
		odds.append(i)

evens = []
for i in abundants:
	if i % 2 == 0:
		evens.append(i)

# take each of these numbers, start adding even abundant numbers to it until sum gets too high

yup = []
for i in odds:
	for j in evens:
		add = i+j
		if add < 20172 and add not in yup: # no duplicates
			yup.append(add)
yup.sort()

odders = range(1, 20172, 2)
almost = []
for i in odders:
	if i not in yup:
		almost.append(i)

f = open('/almost.txt', 'r')

for line in f:
	raw = str(line)
	strings = raw.split(', ')
	
numbers = []

for i in strings:
	n = int(i)
	numbers.append(n)

print sum(numbers) + sum(range(0, 30, 2)) + 34 + 46 - 24 # 12 + 12 works

print "Time: ", '%3d' %(time() - start), "seconds"