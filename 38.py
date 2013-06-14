# What is the largest 1 to 9 pandigital that can be formed by multiplying a fixed number by 1, 2, 3, ... ?

# Try 3-digit numbers only

def checker(s):
	if s.count('1') == 1 and s.count('2') == 1 and s.count('3') == 1 and s.count('4') == 1 and s.count('5') == 1 and s.count('6') == 1 and s.count('7') == 1 and s.count('8') == 1 and s.count('9') == 1:
		return True
	else:
		return False

pandigitals = []

for i in range(1000, 10001):
	one = i * 1
	two = i * 2
	if checker(str(one) + str(two)) == True:
		print i, str(one) + str(two)
		pandigitals.append(int(str(one) + str(two)))
		
for i in range(100, 1001):
	one = i * 1
	two = i * 2
	three = i * 3
	if checker(str(one) + str(two) + str(three)) == True:
		print i, str(one) + str(two) + str(three)
		pandigitals.append(int(str(one) + str(two) + str(three)))

for i in range(10, 101):
	one = i * 1
	two = i * 2
	three = i * 3
	four = i * 4
	if checker(str(one) + str(two) + str(three) + str(four)) == True:
		print i, str(one) + str(two) + str(three) + str(four)
		pandigitals.append(int(str(one) + str(two) + str(three) + str(four)))
		
for i in range(1, 11):
	one = i * 1
	two = i * 2
	three = i * 3
	four = i * 4
	five = i * 5
	six = i * 6
	seven = i * 7
	eight = i * 8
	if checker(str(one) + str(two) + str(three) + str(four) + str(five) + str(six) + str(seven) + str(eight)) == True or checker(str(one) + str(two) + str(three) + str(four) + str(five) + str(six) + str(seven)) == True or checker(str(one) + str(two) + str(three) + str(four) + str(five) + str(six)) == True or checker(str(one) + str(two) + str(three) + str(four) + str(five)) == True:
		print i, str(one) + str(two) + str(three) + str(four) + str(five)

print max(pandigitals)