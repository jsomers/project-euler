# Find n <= 1,000,000 s.t. n/phi(n) is maximized.
import sys
from itertools import groupby
from math import sqrt, floor

_primeslist = [2, 3, 5, 7, 11, 13, 17, 19]
_primeset = set(_primeslist)

def intsqrt(n):
    """intsqrt(n): integer square root of a long number."""
    def intsqrt_core(digitpair, remainder, results):
        if digitpair < 100:
            currvalue = remainder * 100 + digitpair
            for d in xrange(9, -1, -1):
                x = (2 * 10 * results + d) * d
                if x <= currvalue:
                    remainder = currvalue - x
                    results = results * 10 + d
                    return results, remainder
        else:
            div, rem = divmod(digitpair, 100)
            results, remainder = intsqrt_core(div, remainder, results)
            results, remainder = intsqrt_core(rem, remainder, results)
            return results, remainder
    results, remainder = intsqrt_core(n, 0, 0)
    return results

def isPrime(n):
    # Say that 1 and 2 are prime.
    if n==1 or n==2:
        return True
    # If even, it's obviously composite.
    if (n % 2) == 0:
        return False
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
            return False
    else:
        return True

def allfactors(n):
    """allfactors(n): return the list of all the prime factors of n."""
    maxindex = len(_primeslist)
    primes = []
    index = 0
    candidate = _primeslist[index]
    while not primes and candidate <= n: # "not primes" returns True while primes is empty.
        if not(n % candidate) and (index < maxindex
                                   or isPrime(candidate)):
            primes.append(candidate)
            primes.extend(allfactors(n // candidate))
        index += 1
        if index < maxindex:
            candidate = _primeslist[index]
        else:
            candidate += 2
    return primes

def factors(n):
    """Condensed prime factors list in [power, nth_power] format."""
    result = []
    for prime, prime_group in groupby(allfactors(n)):
        npower = 0
        for _ in prime_group:
            npower += 1
        result.append([prime, npower])
    return result

def totient(n):
	if isPrime(n) == True:
		return n-1
	mults = [n]
	for i in range(len(factors(n))):
		mults.append(1-(1./factors(n)[i][0]))
	return reduce(lambda x, y: x*y, mults)
	
print totient(13082761331670030)