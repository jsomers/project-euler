#  361, 381, 401, 421, 441
from math import log
from time import time
start = time()

def primes_below_n(n):
	return n/log(n)

print primes_below_n(10)

diags = []
diags.append(1)
for n in range(3, 50001, 2):
	diags.append(n**2)
	diags.append(n**2 - n + 1)
	diags.append(n**2 - 2*n + 2)
	diags.append(n**2 - 3*n + 3)

diags.sort()

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

pr_ct = 0
for i in range(1, 19000):
	for n in diags[4*(i-1):4*i]: # add primes *as you go along*
		if rm_test(n) == 1:
			pr_ct += 1
	if float(pr_ct-1)/(len(diags[:4*i])+1) < .10:
		print 'Side length:', 2*i+1, 'Primes:', pr_ct-1, 'Diagonals:', len(diags[:4*i])+1, 'Ratio:', float(pr_ct-1)/(len(diags[:4*i])+1), 'Time:', time() - start