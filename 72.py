# How many elements would be contained in the set of reduced proper fractions for d <= 1,000,000?
# Quite slow

def npf(dmax):
    "npf = sum(totient(n) for n in xrange(2, dmax + 1))"
    # calculate totient(n) for n=2..N
    N = dmax + 1; totient = range(N)
    for n in xrange(2, N):
	print totient
        if totient[n] == n:
            for k in xrange(n, N, n):
                totient[k] *= (n - 1);
                totient[k] //=  n;
    # find number of reduced proper fraction
    return sum(totient[2:])

print npf(8)
'''
from totient import *
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

def tri(n):
	return (n**2 + n)/2

atoms = [(1, 2)]

for new_d in range(3, 900):
	if rm_test(new_d) == 1:
		for n in range(1, new_d):
			atoms.append((n, new_d))
	else:
		not_list = []	
		for atom in atoms:
			if float(new_d) / atom[1] % 1. == 0:
				not_list.append((new_d / atom[1]) * atom[0])
			if atom[1] > new_d/2:
				break
		ns = [n for n in range(1, new_d) if n not in not_list]
		for n in ns:
			atoms.append((n, new_d))
	print new_d, len(atoms)

# Other way
tot = 0
for i in range(2, 1000001):
	tot += totient(i)
	if i % 10000. == 1:
		print i, tot
'''