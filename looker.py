# library functions
from random import randint, normalvariate
from math import sqrt, exp, ceil

# generate challenges
challenges = []
for i in range(100):
	challenges.append(randint(0,100))

# normal curve
rt2 = sqrt(2.)
def erfcc(x):
	z = abs(x)
	t = 1. / (1. + 0.5*z)
	r = t * exp(-z*z-1.26551223+t*(1.00002368+t*(.37409196+
		t*(.09678418+t*(-.18628806+t*(.27886807+
		t*(-1.13520398+t*(1.48851587+t*(-.82215223+
		t*.17087277)))))))))
	if (x >= 0.):
		return r
	else:
		return 2. - r
def ncdf(x):
	global rt2
	return 1. - 0.5*erfcc(x/rt2)

# find expected payoff given a, b, challenge, profit and cost functions
def E(a, b, x):
	mu = (b + a)/2.
	stdev = (b - mu)/3
	thepi = x
	k = 5. * exp(x / 35.)
	z_score = (x - mu) / stdev
	F_x = ncdf(z_score)
	return -k*F_x + (1.-F_x)*thepi

# run through (single-agent)
def play(a, b, ability, payoff, period):
	if period >= 100:
		return payoff
	x = challenges[period]
	k = 5. * exp(x / 35.)
	if x <= a:
		payoff += x - k
		return play(a, b, ability, payoff, period+1)
	if x >= b:
		return play(a, b, ability, payoff, period+1)
	if E(a, b, x) > 0 and x>= a and x<= b:
		if x >= ability:
			payoff -= k
			return play(a, x, ability, payoff, period+1)
		elif x <= ability:
			payoff += x - k
			return play(x, b, ability, payoff, period+1)
	elif E(a, b, x) < 0 and x>= a and x<= b:
			return play(a, b, ability, payoff, period+1)

player = int(ceil(normalvariate(50, 17)))
print 'player 1', player
print play(0, 100, player, 0, 0)

def genius(a, b, ability, payoff, period):
	if period == 100:
		return payoff
	x = challenges[period]
	k = 5. * exp(x / 35.)
	ignore = play(a, b, ability, payoff, period+1)
	accept = play(a, b, ability, payoff, period)
	if ignore > accept:
		return genius(a, b, ability, payoff, period+1)
	elif ignore <= accept:
		if x <= a:
			payoff += x - k
			return genius(a, b, ability, payoff, period+1)
		if x >= b:
			return genius(a, b, ability, payoff, period+1)
		if E(a, b, x) > 0 and x>= a and x<= b:
			if x >= ability:
				payoff -= k
				return genius(a, x, ability, payoff, period+1)
			elif x <= ability:
				payoff += x - k
				return genius(x, b, ability, payoff, period+1)
		elif E(a, b, x) < 0 and x>= a and x<= b:
				return genius(a, b, ability, payoff, period+1)

player2 = int(ceil(normalvariate(50, 17)))
print 'player 2', player

print genius(0, 100, player, 0, 0)