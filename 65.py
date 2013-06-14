# Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

from math import ceil

def sum_digits(n):
	tot = 0
	for i in range(10):
		tot += i*str(n).count(str(i))
	return tot

def cont(a, b, c, A, i):
	print a, b, c
	if i == -1:
		return sum_digits(a*c + b)
	new_b = c
	new_c = a*c + b
	new_a = A[i]
	return cont(new_a, new_b, new_c, A, i-1)

A = [n for n in range(102)]

for n in range(102):	
	if n == 0:
		A[n] = 2
	if n % 3. == 1:
		A[n] = int(n - ceil(n/3.))
	else:
		A[n] = 1
A.pop(0)
A.pop(0)
A[0] = 2
print A
print cont(A[len(A)-2], 1, A[len(A)-1], A, len(A)-3)