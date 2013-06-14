# How many lengths of wire N <= 1,000,000 can be bent into just one right triangle?
def gcd(a, b):
     while b != 0:
         t = b
         b = a % b
         a = t
     return a

primitives = []
for m in range(1, 707):
	""" Generate primitive Pythagorean triples """
	for n in range(1, m):
		if gcd(m, n) == 1 and ( m % 2. == 0 or n % 2. == 0 ):
			a = ( m**2 - n**2 )
			b = 2*m*n
			c = m**2 + n**2
			if ( a + b + c ) < 10**6:
				primitives.append(sum([a, b, c]))
			else:
				pass
				
primitives.sort()

zeroes = [0]*(10**6+1)

for primitive in primitives:
	for n in range(primitive, 10**6 + 1, primitive): #check every multiple
		zeroes[n] += 1

ct=0
for i in zeroes:
	if i == 1:
		ct+=1

print ct