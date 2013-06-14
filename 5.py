# What is the smallest number that is evenly divisible by all of the numbers from 1 to 20?

start = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 * 11 * 12 * 13 * 14 * 15 * 16 * 17 * 18 * 19 * 20

def good(x):
	if x % 1 == 0 and x % 2 == 0 and x % 3 == 0 and x % 4 == 0 and x % 5 == 0 and x % 6 == 0 and x % 7 == 0 and x % 8 == 0 and x % 9 == 0 and x % 10 == 0 and x % 11 == 0 and x % 12 == 0 and x % 13 == 0 and x % 14 == 0 and x % 15 == 0 and x % 16 == 0 and x % 17 == 0 and x % 18 == 0 and x % 19 == 0 and x % 20 == 0:
		print "true"
	else:
		print "false"
		
def tester(low, number):
	if low > 21:
		return number
	x = number/float(low)
	if x % low == 0:
		print x, good(x)
		tester(low+1, x)
		
tester(2, 232792560) # put start here, use "good" to find out if it's cool... plug lowest "true" in for "start"