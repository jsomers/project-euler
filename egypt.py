#!/usr/bin/env python

"""
Egypt -- command line Egyptian fraction generator
D. Eppstein, UC Irvine, 5 Mar 2004
"""

from __future__ import division

from optparse import OptionParser
from random import randint
import operator
import sys
import math

# ======================================================================
#   Basic utility subroutines
# ======================================================================

def count(n = 0):
    """
    Generate successive integers starting with n.
    Just like itertools.count except that n can be a long.
    """
    while True:
        yield n
        n += 1

def intString(x):
    """
    String for integer x, obeying options.factor.
    """
    if x < 2 or not options.factor:
        return str(x)
    factorization = itemCounts(factors(x)).items()
    factorization.sort()
    out = []
    for p,e in factorization:
        if e > 1:
            out.append("%d^%d" % (p,e))
        else:
            out.append(str(p))
    return ".".join(out)

def unitFractionString(dd):
    """
    Construct string for 1/dd.
    """
    if dd == 1:
        return "1"
    else:
        return "1/" + intString(dd)

def egyptianFractionString(xx):
    """
    Construct string for Egyptian fraction formed by list of denominators in xx.
    """
    return " + ".join(map(unitFractionString,xx))


# ======================================================================
#   Backtracking search structure
# ======================================================================

def ok(xx,dd):
    """
    Test whether we can extend Egyptian fraction xx by appending dd.
    Checks for duplications and violations of constraints in command-line options.
    Returns True if dd can be appended, False otherwise.
    """
    if dd < 1:
        return False
    if options.odd and dd % 2 == 0:
        return False
    if options.square and isqrt(dd)**2 != dd:
        return False
    if options.length and len(xx) >= options.length:
        return False
    if options.maxden and dd > options.maxden:
        return False
    if options.minden and dd < options.minden:
        return False
    if not options.repeat and dd in xx:
        return False
    return True 

def noSolutions():
    """
    Return empty stream of Egyptian fraction solutions.
    """
    return iter([])
    
def singleSolution(xx):
    """
    Return stream consisting of the single Egyptian fraction solution xx.
    """ 
    yield xx
    return
    
def trySolution(xx):
    """
    Test if solution xx is ok and if so return stream with that single solution.
    """
    zz = []
    for den in xx:
        if not ok(zz,den):
            return noSolutions()
        zz.append(den)
    return singleSolution(zz)

def tryUnit(xx,nn,dd,den):
    """
    Attempt to use den as the first term in an Egyptian fraction for nn/dd.
    Should be called from the function stored in the method global variable.
    method(xx,nn,dd) searches for denominators to use in expanding nn/dd,
    with xx consisting of unit fractions already included in the current
    solution and nn/dd representing the remaining fraction after those
    unit fractions have been subtracted from the input.  For each
    possible denominator den, method(xx,nn,dd) should call
    tryUnit(xx,nn,dd,den), and pass the resulting stream of solutions to
    its own output stream.  tryUnit(xx,nn,dd,den) will attempt to add den
    to the partial solution in xx, update nn and dd, and then call
    method(xx,nn,dd) on the updated values xx,nn,dd recursively.
    """
    if not ok(xx,den):
        return noSolutions()
    nn = nn*den - dd
    if nn < 0:
        return noSolutions()
    xx = xx + (den,)
    if nn == 0:
        return singleSolution(xx)
    dd *= den
    g = gcd(nn,dd)
    nn,dd = nn//g, dd//g
    if options.verbose:
        print >>sys.stderr, "Trying", egyptianFractionString(xx), \
            "+", intString(nn)+"/"+intString(dd)
    if options.length:
        if len(xx) + estimatedLength(nn,dd) > options.length:
            return noSolutions()
        if len(xx) + 2 == options.length and method == egypt_greedy:
            return egypt_reduce(xx,nn,dd)   # speed up without changing solution set
        if len(xx) + 1 == options.length:
            if nn != 1 or not ok(xx,dd):
                return noSolutions()
            return singleSolution(xx+(dd,))
    return method(xx,nn,dd)

def mustBeEven():
    """
    Generate a warning message for methods unable to produce only odd numbers.
    """
    if options.odd:
        print "Method is incompatible with odd restriction."
        sys.exit(0)

def mustBeSmall(n):
    """
    Generate a warning message for methods unable to handle large numbers.
    """
    print "Unable to handle inputs >=",n,"with these settings."
    sys.exit(0)

def estimatedLength(nn,dd):
    """
    Generate a conservative underestimate of the number of terms
    needed in any Egyptian fraction expansion of nn/dd.
    The idea is to let 1/u be the nearest unit fraction greater than nn/dd,
    and generate a greedy expansion that reaches a number in the
    half-open interval [nn/dd,1/u).  Note that the terms of this expansion
    depend only on u; the inputs nn and dd are used only to compute u and
    to terminate the expansion (when it sums to at least nn/dd).
    """
    if nn <= 1:
        return nn
    u = dd//nn
    nterms = 0
    while True:
        nterms += 1
        t = u + 1
        nn = nn*t - dd
        if nn <= 0:
            return nterms
        dd *= t
        u *= t


# ======================================================================
#   Pollard Rho factorization from Kirby Urner,
#   http://www.mathforum.org/epigone/math-teach/blerlplerdghi
# ======================================================================

def gen(n,c=1):
    """
    Generate sequence x_i = (x_{i-1}^2 + c) mod n
    Where n is the target composite we want to factor.
    """
    x = 1
    while True:
        x = (x**2 + c) % n
        yield x

def rho(n, maxt=500, maxc=10):
    """
    Pollard's Rho method for factoring n.
    Returns a list of factors (not necessarily prime) of n.
    Tests each polynomial x^2+c (c in range(1,maxc))
    by following the sequence gen(n,c) for maxt steps.
    If the sequence is cyclic modulo a factor of n
    with a smaller cycle length than its cycle modulo n,
    we can identify a factor of n as the gcd of n
    with the difference of two sequence values separated
    by the smaller cycle length in the sequence.
    """
    if millrab(n):  # don't bother with probable primes
        return [n]
    for c in range(1,maxc):
        seqslow = gen(n,c) 
        seqfast = gen(n,c)
        for trial in range(maxt):
            xb = seqslow.next()     # slow generator goes one step
            seqfast.next()
            xk = seqfast.next()     # while fast generator goes two
            diff = abs(xk-xb)
            if not diff:
                continue
            d = gcd(diff,n)         # have a factor?
            if n>d>1:                
                return [d,n//d]
    return [n]    # failure to factor
    
def gcd(a,b):
    """
    Euclid's algorithm for integer greatest common divisors.
    """
    while b:
        a,b = b,a%b
    return a

def millrab(n, max=30):
    """
    Miller-Rabin primality test as per the following source:
    http://www.wikipedia.org/wiki/Miller-Rabin_primality_test
    Returns probability p is prime: either p = 0 or ~1,
    """
    if not n%2: return 0
    k = 0
    z = n - 1

    # compute m,k such that (2**k)*m = n-1
    while not z % 2:
      k += 1
      z //= 2
    m = z

    # try tests with max random integers between 2,n-1
    ok = 1
    trials = 0
    p = 1
    while trials < max and ok:
        a = randint(2,n-1)
        trials += 1
        test = pow(a,m,n)
        if (not test == 1) and not (test == n-1):
            # if 1st test fails, fall through
            ok = 0
            for r in range(1,k):
                test = pow(a, (2**r)*m, n)
                if test == (n-1):
                    ok = 1 # 2nd test ok
                    break
        else: ok = 1  # 1st test ok
        if ok==1:  p *= 0.25
            
    if ok:  return 1 - p
    else:   return 0


# ======================================================================
#   Integer factorization and divisor enumeration
# ======================================================================

# Find all factors and divisors
# Fix rho (doesn't handle powers of two correctly) and speed up small primes

def factors(n):
    """
    Return a list of the factors of n.
    Uses trial division for small primes before switching to Pollard's Rho method.
    """
    f = []
    for p in [2,3,5,7,11,13,17,19]:
        while n % p == 0:
            f.append(p)
            n //= p
    if n == 1:
        return f
    if millrab(n):
        return f + [n]
    maxt,maxc = 100,5
    rho_results = [n]
    while len(rho_results) == 1:
        rho_results = rho(n,maxt,maxc)
        maxt *= 2
        maxc *= 2
    for factor in rho_results:
        f += factors(factor)
    return f

def itemCounts(S):
    """
    Return dictionary mapping items in S to how many times they occur in S.
    """
    items = {}
    for x in S:
        items[x] = items.get(x,0) + 1
    return items

def subcounts(D):
    """
    Generates sequence of all maps dominated by a map D from items to numbers.
    That is, each output is a dictionary that maps the same items to numbers,
    and all numbers in each output dictionary are at most equal to the
    corresponding number in the input dictionary.
    """
    if not D:
        yield {}
        return
    x = min(D)
    n = range(D[x]+1)
    del D[x]
    for dd in subcounts(D):
        for i in n:
            dd[x] = i
            yield dd

def divisors(n):
    """
    Generate sequence of all divisors of n.
    """
    for dd in subcounts(itemCounts(factors(n))):
        yield reduce(operator.mul,[x**i for x,i in dd.items()],1)

def primepowers(n):
    """
    Prime power factors of n.
    """
    return [x**y for x,y in itemCounts(factors(n)).iteritems()]
