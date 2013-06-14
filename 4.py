# Find the largest palindrome made from the product of two 3-digit numbers.

numbers = []
palindromes = []
palinints = []

# find all products of 3-digit numbers
for i in range(100, 999):
	for j in range(100, 999):
		numbers.append(i*j)

for index in range(len(numbers)):
	value = numbers[index]
	string = str(value)	# turn all the numbers into strings
	reverse = string[::-1]	#  reverse the strings... Extended Slices: http://www.python.org/doc/2.3.5/whatsnew/section-slices.html
	if reverse == string:	# if reverse is the same as the string (i.e., palindrome tester):
		palinints.append(int(string))	# collect palindromic numbers as ints
		palindromes.append(string)		# collect palindromic numbers as strings	
print palindromes[:100]	
print "string max", max(palindromes)
print "number max", max(palinints)