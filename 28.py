# What is the sum of both diagonals in a 1001 by 1001 spiral formed in the same way?
# 1,002,001
diags = []
def diag(a, b, c, d, ctr):
	if ctr > 4000:
		return
	new_a = a + ctr
	ctr += 2
	
	new_b = b + ctr
	ctr += 2
	
	new_c = c + ctr
	ctr += 2
	
	new_d = d + ctr
	ctr += 2
	diags.append(new_a)
	diags.append(new_b)
	diags.append(new_c)
	diags.append(new_d)
	diag(new_a, new_b, new_c, new_d, ctr)

diag(1, 1, 1, 1, 0)
print diags
print sum(diags[0:2001])