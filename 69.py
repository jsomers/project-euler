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
    """Return True if n is prime."""
    if n in _primeset:
        return True
    high = intsqrt(n)
    for x in _primeslist:
        if x <= high and not(n % x): # if the prime divides n (i.e., n % x == 0), FALSE
            return False
        if x >= high: # if no prime divides n
            return True
    x = _primeslist[-1] + 2 # if you don't have enough primes, go by two
    while x <= high:
        if not(n % x):
            return False
        x += 2
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
	
totient_rats = []
for D in range(2*3*5*7*11*13*17, 1000001, 1024):
	multlist = [D]
	for i in range(len(factors(D))):
		multlist.append(1-(1./factors(D)[i][0]))
	print D, D/reduce(lambda x, y: x*y, multlist)
	totient_rats.append((D/reduce(lambda x, y: x*y, multlist), D))

print max(totient_rats)

# Sample output:
#
# python factorize.py 173248246132375748867198458668657948626531982421875
# [[3, 24], [5, 14], [7, 33], [13, 1]]
# python factorize.py 10969629647
# [[104729, 1], [104743, 1]]