"""Compute solutions to the diophantine Pell equation x^2-D*y^2=1."""

import itertools

def pell (D):
    """Return the smallest integer set solving Pell equation
    x^2-D*y^2=1 where x, D and y are positive integers. If there are no
    solution (D is a square), return None.

    >>> pell(3)
    (2, 1)"""
    a0 = int (D**0.5)
    if a0*a0 == D: return None
    gp = [0, a0]
    gq = [1, D-a0**2]
    a = [a0, int((a0+gp[1])/gq[1])]
    p = [a[0], a[0]*a[1]+1]
    q = [1, a[1]]
    maxdepth = None
    n = 1
    while maxdepth is None or n < maxdepth:
        if maxdepth is None and a[-1] == 2*a[0]:
            r = n-1
            if r % 2 == 1: return p[r], q[r]
            maxdepth = 2*r+1
        n += 1
        gp.append (a[n-1]*gq[n-1]-gp[n-1])
        gq.append ((D-gp[n]**2)//gq[n-1])
        a.append (int ((a[0]+gp[n])//gq[n]))
        p.append (a[n]*p[n-1]+p[n-2])
        q.append (a[n]*q[n-1]+q[n-2])
    return p[2*r+1], q[2*r+1]


answers = []
for i in range(1, 1000):
	answers.append((pell(i), i))

answers.sort()
print answers