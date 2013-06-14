# Find the first ten digits of the sum of one-hundred 50-digit numbers.

h = open('/50_big_numbers.txt', 'r')

numbers = []
for line in h:
	raw_string = str(line)
	new_string = raw_string.replace("\n", "")
	numbers.append(int(new_string))

print sum(numbers) # only really need to add the first 11 digits