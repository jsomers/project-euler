# Add all the natural numbers below 1000 that are multiples of 3 or 5.

# Step 1: create list of all multiples of 3 or 5

three_five = []

for i in range(0,1000):
	t = i%3
	f = i%5
	if t == 0 and f > 0:
		three_five.append(i)
	if f == 0 and t > 0:
		three_five.append(i)
	if t == 0 and f == 0:
		three_five.append(i)
		
# Step 2: add up the values in the list

print sum(three_five)
# print sum([i for i in range(1000) if not i % 5 or not i % 3])