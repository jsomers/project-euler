# Investigating putting coins into piles
# The key is to run Euler's recursive algorithm in Mod 1M

class Memoize:
    def __init__(self, func): 
        self.func = func
        self.cache = {}
    def __call__(self, arg):
        if arg not in self.cache: 
            self.cache[arg] = self.func(arg)
        return self.cache[arg]

@Memoize
def p(n):
    if n<0: return 0
    if n<2: return 1
    sm=0
    for k in xrange(1, n+1):
        n1 = n-k*(3*k-1)/2
        n2 = n-k*(3*k+1)/2
        sm += (-1)**(k+1) * (p(n1) + p(n2))
        if n1 <= 0:
            break
    return sm%1000000

n=0
while p(n)!=0: n += 1
print n