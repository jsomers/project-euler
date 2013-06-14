# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
from time import time
start = time()
h = open('/primes.txt', 'r')
primes = []
for line in h:
	raw_string = str(line)
	new_string = raw_string.replace("\n", "")
	primes.append(int(new_string))

def rm_test(n):
    # Say that 1 and 2 are prime.
    if n==1 or n==2:
        return 1

    # If even, it's obviously composite.
    if (n % 2) == 0:
        return 0

    # Straightforward Rabin-Miller test...
    # Compute r,s, such that N = s*2**r + 1.
    n1 = n-1
    r = 1
    while 1:
        div = n1/(2**r)
        if div*(2**r) != n1:
            break
        r += 1

    r = r-1 ; s = n1/(2**r)

    # Try a bunch of integers.  If a**s == 1, or
    # a**(s*2**j) == -1, for j in 0...r, the
    # number is prime.  (Trying more values of 'a' 
    # will decrease the risk that n isn't really prime.)
    for a in range(2, min(10,n)):
        t1 = pow(a,s,n)
        if t1 == 1:
            continue
        prime = 0
        for j in range(0, r):
            t2 = pow(a, s*(2**j), n)
            if t2 == (n-1):
                prime=1
                break
        else:
            return 0
    else:
        return 1

def sum_digits(n):
	a = 0
	for e in list(str(n)):
		a += int(e)
	return a

candidates = []
for n in primes[:10000]:
	if sum_digits(n)%3. == 1 or sum_digits(n)%3.==0:
		candidates.append(n)

def concat(a, b):
	if rm_test(int(str(a) + str(b))) == 1 and rm_test(int(str(b) + str(a))) == 1:
		return True
	else:
		return False
		
def finish(L, e):
	a = L[0]
	b = L[1]
	c = L[2]
	d = L[3]
	if rm_test(int(str(a) + str(b))) == 1 and rm_test(int(str(b) + str(a))) == 1 and rm_test(int(str(a) + str(c))) == 1 and rm_test(int(str(c) + str(a))) == 1 and rm_test(int(str(a) + str(d))) == 1 and rm_test(int(str(d) + str(a))) == 1 and rm_test(int(str(a) + str(e))) == 1 and rm_test(int(str(e) + str(a))) == 1 and rm_test(int(str(b) + str(c))) == 1 and rm_test(int(str(c) + str(b))) == 1 and rm_test(int(str(b) + str(d))) == 1 and rm_test(int(str(d) + str(b))) == 1 and rm_test(int(str(b) + str(e))) == 1 and rm_test(int(str(e) + str(b))) == 1 and rm_test(int(str(c) + str(d))) == 1 and rm_test(int(str(d) + str(c))) == 1 and rm_test(int(str(c) + str(e))) == 1 and rm_test(int(str(e) + str(c))) == 1 and rm_test(int(str(d) + str(e))) == 1 and rm_test(int(str(e) + str(d))) == 1:
		return True
	else:
		return False

print finish([7, 1237, 2341, 12409], 18433)
a = 13
for b in candidates[candidates.index(a):]:
	if concat(a, b) == True:
		for c in candidates[candidates.index(b):]:
			if concat(a, c) == True and concat(b, c) == True:
				if a + b + 3*c > 35000:
					break
				for d in candidates[candidates.index(c):]:
					if concat(a, d) == True and concat(b, d) == True and concat(c, d) == True:
						for e in candidates[candidates.index(d):]:
							if concat(a, e) == True and concat(b, e) == True and concat(c, e) == True and concat(d, e) == True:
								print a, b, c, d, e, sum([a, b, c, d, e]), start-time(), 'seconds'
