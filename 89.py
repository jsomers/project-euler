def numerize(s):
	s.strip()
	n = 0
	n += 4 * s.count('IV')
	s1 = s.replace('IV', '')
	n += 9 * s1.count('IX')
	s2 = s1.replace('IX', '')
	n += 40 * s2.count('XL')
	s3 = s2.replace('XL', '')
	n += 90 * s3.count('XC')
	s4 = s3.replace('XC', '')
	n += 400 * s4.count('CD')
	s5 = s4.replace('CD', '')
	n += 900 * s5.count('CM')
	s6 = s5.replace('CM', '')
	n += 1 * s6.count('I')
	n += 5 * s6.count('V')
	n += 10 * s6.count('X')
	n += 50 * s6.count('L')
	n += 100 * s6.count('C')
	n += 500 * s6.count('D')
	n += 1000 * s6.count('M')
	return n

def romanize(n):
	s = ''
	s += 'M' * (n // 1000)
	n = n % 1000
	s += 'CM' * (n // 900)
	n = n % 900
	s += 'D' * (n // 500)
	n = n % 500
	s += 'CD' * (n // 400)
	n = n % 400
	s += 'C' * (n // 100)
	n = n % 100
	s += 'XC' * (n // 90)
	n = n % 90
	s += 'L' * (n // 50)
	n = n % 50
	s += 'XL' * (n // 40)
	n = n % 40
	s += 'X' * (n // 10)
	n = n % 10
	s += 'IX' * (n // 9)
	n = n % 9
	s += 'V' * (n // 5)
	n = n % 5
	s += 'IV' * (n // 4)
	n = n % 4
	s += 'I' * (n // 1)
	return s

f = open('./roman.txt', 'rU')

tot = 0
for line in f:
#	print len(line) - 1, line, len(romanize(numerize(line))), romanize(numerize(line))
	tot += (len(line) - 1) - len(romanize(numerize(line)))

print tot