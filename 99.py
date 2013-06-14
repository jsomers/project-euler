# determine which line number has the greatest numerical value.
from math import log
f = open('/base_exp.txt', 'rU')

pairs = []
for line in f:
	pairs.append(line.split(','))

tots = []
for pair in pairs:
	tots.append(int(pair[1].replace('\n', ''))*log(int(pair[0])))

print tots.index(max(tots))