# How many Lychrel numbers are there below ten-thousand?

def is_palindrome(s):
	if s == s[::-1]: return 1
	else: return 0

def do(n):
	return lychrel(n, 1)

hits = []

def lychrel(n, its):
	if its > 50:
		hits.append(1)
		return
	rev = int("".join(map(str, list(str(n))[::-1])))
	
	if is_palindrome(str(rev + n)) == 1: return its
	
	else: return lychrel(n+rev, its+1)


for i in range(10000): do(i)

print len(hits)