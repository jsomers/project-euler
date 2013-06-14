# Find the smallest prime which, by changing the same part of the number, can form eight different primes.

from time import time
start = time()
h = open('/primes.txt', 'r')
primes = []

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

for line in h:
	raw_string = str(line)
	new_string = raw_string.replace("\n", "")
	primes.append(int(new_string))

# Speed improvement: if it doesn't find it by the time you clear the first significant digits (through 2), it won't!
for n in primes[9593:25998]: # six-digit primes
	fails = 0
	digits = list(str(n))
	for j in range(10):
		if fails > 2:
			break
		# specify what to replace
		digits[0] = str(j)
		digits[2] = str(j)
		digits[4] = str(j)
		new_num = int("".join(map(str, digits)))
		if rm_test(new_num) == 0:
			fails += 1
	if fails <= 2:
		print n, 'success'

print time() - start, 'seconds'