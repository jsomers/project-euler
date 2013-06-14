# Find the value of D <= 1000 in minimal solutions of x for which the largest value of x is obtained. (to the Pell equation x^2 - Dy^2 = 1)
from math import ceil, floor, sqrt

def is_square(n):
	if ceil(pow(n, 1./2))**2 == n:
		return True
	else:
		return False

def cont_frac(n):
	A = [floor(sqrt(n))]
	B = [1]
	C = [floor(sqrt(n))]
	for i in range(1, 2000):
		A.append(long(floor((B[i-1]*(floor(sqrt(n)) + C[i-1]))/(n-C[i-1]**2))))
		B.append((n - C[i-1]**2)/B[i-1])
		C.append(abs(C[i-1] - (A[i]*(n - C[i-1]**2)/B[i-1])))
	return A

def convergents(A):
	HKs = []
	HKs.append((long(A[0]), 1))
	HKs.append((long(A[0]*A[1] + 1), long(A[1])))
	HKs.append((long(A[2]*(A[0]*A[1] + 1) + A[0]), long(A[2]*A[1] + 1)))
	for i in range(3, 300):
		HKs.append((long(A[i]*HKs[i-1][0] + HKs[i-2][0]), long(A[i]*HKs[i-1][1] + HKs[i-2][1])))
	return HKs

Ds = [a for a in range(1, 1001) if is_square(a) == False]
finds = []
Dused = []
for D in Ds:
	A = cont_frac(D)
	for HK in convergents(A):
		h = HK[0]
		k = HK[1]
		if h**2 - k**2*D == 1:
			print h, D, k, h**2 - k**2*D
			Dused.append(D)
			finds.append([h, D])
			break

print [a for a in Ds if a not in Dused]
finds.sort()
print finds