from math import sqrt
from time import time

start = time()
words = [a.replace('"', '') for a in open('words.txt', 'r').read().split(',')]
alphabet = [a.upper() for a in list('abcdefghijklmnopqrstuvwxyz')]

def are_anagrams(word1, word2):
	for letter in alphabet:
		if word1.count(letter) != word2.count(letter):
			return False
	if len(word1) == len(word2):
		return True

def is_square(n):
	if sqrt(n) % 1 == 0:
		return True
	else:
		return False

def is_square_pair(word1, word2, square):
	tupes = zip(list(word1), list(str(square)))
	the_dict, check_dict = {}, {}
	for tupe in tupes:
		the_dict[tupe[0]] = tupe[1] # D['A'] = 1
		if check_dict.has_key(tupe[1]):
			if check_dict[tupe[1]] != tupe[0]:
				return False
			else:
				continue
		else:
			check_dict[tupe[1]] = tupe[0]
	new_square_string = ''
	for letter in word2:
		new_square_string += the_dict[letter]
	if is_square(int(new_square_string)) and len(str(square)) == len(str(int(new_square_string))):
		return [square, int(new_square_string)]
	else:
		return False

def make_anagram_pairs():
	pairs = []
	for i, word1 in enumerate(words):
		for word2 in words[i + 1:]:
			if are_anagrams(word1, word2):
				pairs.append((word1, word2))
	return pairs

squares_of_length = {}
for i in xrange(100000000):
	square = i ** 2
	if len(str(square)) < 10:
		try:
			squares_of_length[len(str(square))].append(square)
		except:
			squares_of_length[len(str(square))] = []
	else:
		break

squares = []
pairs = make_anagram_pairs()
for pair in pairs:
	square_list = squares_of_length[len(pair[0])]
	for square in square_list:
		is_square_p = is_square_pair(pair[0], pair[1], square)
		if is_square_p:
			#print pair[0], pair[1], max(is_square_p)
			squares.append(max(is_square_p))


#print 8973.0 ** 2, 80514729

#print is_square_pair('CREATION', 'REACTION', 80514729)

print time() - start, max(squares)