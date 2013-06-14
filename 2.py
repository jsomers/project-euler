# Find the sum of all the even-valued terms in the Fibonacci sequence which do not exceed one million.

fibs = []
final = []

# Step 1: make a list of Fibonacci numbers up to 1,000,000
def fib_list(p, q, a, count):
	if a >= 1000000:
		return
	a = p + q
	fibs.append(a)
	fib_list(q, a, a, count+1)
	p = q
	q = a

fib_list(1, 1, 0, 0)
# Step 2: get rid of the last Fibonacci number, which is greater than 1,000,000
fibs.pop()

# Step 3: make a new list "final" that only has even members of "fibs"
for index in range(len(fibs)):
	value = fibs[index]
	mod = value % 2
	if mod == 0:
		final.append(value)

print fibs
print final

print sum(final)