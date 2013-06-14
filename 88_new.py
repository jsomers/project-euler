from math import floor
import psyco
psyco.full()

def prod(ls):
	return reduce(lambda x, y: x * y, ls[0])

def formula(ls):
	a = int(floor(ls[0][0] * ((sum(ls[0]) + ls[1]) - prod(ls)) / prod(ls))) + 1
	ls[0][0] += a
	if (sum(ls[0]) + ls[1]) >= prod(ls):
		return ls
	else:
		return False

def copyleft(ls, index):
	a = ls[0][index] + 1
 	new = ([a] * (index + 1) + ls[0][index + 1:], ls[1])
	if (sum(new[0]) + new[1]) >= prod(new):
		return new
	else:
		return False

def baseshift(ls):
	new = copyleft(ls, ls[0].index(1))
	if new and (sum(new[0]) + new[1]) >= prod(new):
		return new
	else:
		return False

print '2:', '4 =', '2 x 2'
master = [4]
for n in range(3, 12001):
	# Initial conditions.
	ls = [2, 2] + [1] * (n - 2)
	if len(ls) >= 20:
		ls = (ls[:20], 	n + 2 - sum(ls[:20]))
	else:
		ls = (ls, 0)

	# 1. Try formula
	# 2. If that fails, try copyleft with index 1
	# 3. If that fails, try copyleft with index 2. If it works, go to step 1.
	# 4. Else, try copyleft with index 3.
	# 5. Else, try copyleft with index 4. Continue trying until index runs into base.
	# 6. Then base shift.

	products = []
	g = True
	while g:
		if prod(ls) == (sum(ls[0]) + ls[1]):
			products.append((prod(ls), ls[0]))
		new = formula(ls)
		if new:
			ls = new
			continue
		else:
			index = 1
			while index + 1 < ls[0].index(1) and not copyleft(ls, index):
				index += 1
			new = copyleft(ls, index)
			if new:
				ls = new
				continue
			else:
				new = baseshift(ls)
				if new:
					ls = new
					continue
				else:
					g = False
	sol = min(products)[1]
	sol = sol[:sol.index(1)]
#	times_string = " x ".join([str(a) for a in sol])
	print "%s: %s" %(n, min(products)[0])
	master.append(min(products)[0])

print sum([a for a in set(master)])