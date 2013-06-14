# How many different ways can one hundred be written as a sum of at least two positive integers?

'''
def findN():
  sequence = [[0], [1]]
  sums = [0, 1]
  n = 2
  while ( True ):
    array = []
    for i in xrange( 1, n ):
      x = n - i
      if ( x <= i ):
        array.append( sums[ x ] )
      else:
        s = 0
        for j in xrange( 0, i ):
          s += sequence[ x ][ j ]
        array.append( s )
    array.append( 1 )
    sequence.append( array )
    sums.append( reduce(lambda x, y: x + y, array) )
    if (n == 100):
      print sums[ -1 ] - 1
      break
    n += 1

findN()
'''
from time import time
start = time()
def place(n, ct = 0):
	if n < 1:
		return ct
	else:
		return place(n/10., ct + 1)

def sum_digits(n):
	tot = 0
	for i in range(10):
		tot += i*str(n).count(str(i))
	return tot

def to_ten(n):
	ten = 0
	for i in range(10):
		ten += str(n).count(str(i)) * 10**i
	return ten

def nexts(n):
	L = []
	p = place(n)
	for i in range(p, -1, -1):
		t = n+10**i
		L.append(t)
	return L

def iterator(L, ct):
	tens = []
	newL = []
	if ct == 10:
		return len(L), time() - start
	for i in L:
		for n in nexts(i):
			if to_ten(n) not in tens and sum_digits(n) == ct + 2 and len(str(n)) > 1:
				newL.append(n)
				tens.append(to_ten(n))
	return iterator(newL, ct + 1)

print iterator([1], 0)