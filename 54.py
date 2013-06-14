# How many hands did player one win in the game of poker?

from time import time
start = time()

print "	Player 1's Hand			Player 2's Hand				Outcome"
print "	---------------			---------------				-------"
h = open('/poker.txt', 'rU')

lines = []
for line in h:
	raw_string = str(line)
	new_string = raw_string.replace("\n", "")
	deal = new_string.split(" ")
	lines.append(deal)

values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

def royal_flush(H):
	pts = 0
	hand = "".join(map(str, H))
	if hand.count('T') == 1 and hand.count('J') == 1 and hand.count('Q') == 1 and hand.count('K') == 1 and hand.count('A') == 1:
		pts+=1
	if hand.count('C') == 5 or hand.count('H') == 5 or hand.count('D') == 5 or hand.count('S') == 5:
		pts+=1
	if pts == 2:
		return 1
	else:
		return 0

def straight_flush(H):
	pts = 0
	hand = "".join(map(str, H))
# straight
	for i in range(9):
		if hand.count(values[i]) == 1 and hand.count(values[i+1]) == 1 and hand.count(values[i+2]) == 1 and hand.count(values[i+3]) == 1 and hand.count(values[i+4]) == 1:
			pts += 1
# flush
	if hand.count('C') == 5 or hand.count('H') == 5 or hand.count('D') == 5 or hand.count('S') == 5:
		pts+=1
	if pts == 2:
		return 1
	else:
		return 0

def four_of_a_kind(H):
	pts = 0
	hand = "".join(map(str, H))
	for i in range(1, 10):
		if hand.count(str(i)) == 4:
			pts+=1
	if hand.count('T') == 4 or hand.count('J') == 4 or hand.count('Q') == 4 or hand.count('K') == 4 or hand.count('A') == 4:
		pts+=1
	if pts == 1:
		return 1
	else:
		return 0

def full_house(H):
	counts = []
	pts = 0
	hand = "".join(map(str, H))
	for value in values:
		counts.append(hand.count(value))
	if counts.count(3) > 0 and counts.count(2) > 0:
		return 1
	else:
		return 0

def flush(H):
	pts = 0
	hand = "".join(map(str, H))
	if hand.count('C') == 5 or hand.count('H') == 5 or hand.count('D') == 5 or hand.count('S') == 5:
		return 1
	else:
		return 0

def straight(H):
	pts = 0
	hand = "".join(map(str, H))
	for i in range(9):
		if hand.count(values[i]) == 1 and hand.count(values[i+1]) == 1 and hand.count(values[i+2]) == 1 and hand.count(values[i+3]) == 1 and hand.count(values[i+4]) == 1:
			pts += 1
	if pts == 1:
		return 1
	else:
		return 0

def three_of_a_kind(H):
	pts = 0
	hand = "".join(map(str, H))
	for value in values:
		if hand.count(value) == 3:
			pts += 1
	if pts == 1:
		return 1
	else:
		return 0

def two_pairs(H):
	pts = 0
	hand = "".join(map(str, H))
	for value in values:
		if hand.count(value) == 2:
			pts +=1
	if pts == 2:
		return 1
	else:
		return 0

def one_pair(H):
	pts = 0
	hand = "".join(map(str, H))
	for value in values:
		if hand.count(value) == 2:
			pts+=1
	if pts == 1:
		return 1
	else:
		return 0

def high_card(H):
	hitlist = []
	pts = 0
	hand = "".join(map(str, H))
	for value in values:
		hitlist.append(hand.count(value))
	for i in hitlist[::-1]:
		if i > 0:
			return len(values) - hitlist[::-1].index(i)
		
P1_hands = 0
P2_hands = 0

for deal in lines:
	P1 = deal[0:5]
	P2 = deal[5:10]
	if royal_flush(P1) == 1 and royal_flush(P2) == 0:
		print P1, P2, 'Player 1 wins with a royal flush'
		P1_hands += 1
	elif royal_flush(P2) == 1 and royal_flush(P1) == 0:
		print P1, P2, 'Player 2 wins with a royal flush'
		P2_hands += 1
	elif royal_flush(P1) == 0 and royal_flush(P2) == 0:
		if straight_flush(P1) == 1 and straight_flush(P2) == 0:
			print P1, P2, 'Player 1 wins with a straight flush'
			P1_hands += 1
		elif straight_flush(P2) == 1 and straight_flush(P1) == 0:
			print P1, P2, 'Player 2 wins with a straight flush'
			P2_hands += 1
		elif straight_flush(P1) == 0 and straight_flush(P2) == 0:
			if four_of_a_kind(P1) == 1 and four_of_a_kind(P2) == 0:
				print P1, P2, 'Player 1 wins with four of a kind'
				P1_hands += 1
			elif four_of_a_kind(P2) == 1 and four_of_a_kind(P1) == 0:
				print P1, P2, 'Player 2 wins with four of a kind'
				P2_hands += 1
			elif four_of_a_kind(P1) == 0 and four_of_a_kind(P2) == 0:
				if full_house(P1) == 1 and full_house(P2) == 0:
					print P1, P2, 'Player 1 wins with a full house'
					P1_hands += 1
				elif full_house(P2) == 1 and full_house(P1) == 0:
					print P1, P2, 'Player 2 wins with a full house'
					P2_hands += 1
				elif full_house(P1) == 0 and full_house(P2) == 0:
					if flush(P1) == 1 and flush(P2) == 0:
						print P1, P2, 'Player 1 wins with a flush'		
						P1_hands += 1
					elif flush(P2) == 1 and flush(P1) == 0:
						print P1, P2, 'Player 2 wins with a flush'
						P2_hands += 1
					elif flush(P1) == 0 and flush(P2) == 0:
						if straight(P1) == 1 and straight(P2) == 0:
							print P1, P2, 'Player 1 wins with a straight'
							P1_hands += 1
						elif straight(P2) == 1 and straight(P1) == 0:
							print P1, P2, 'Player 2 wins with a straight'
							P2_hands += 1
						elif straight(P1) == 0 and straight(P2) == 0:
							if three_of_a_kind(P1) == 1 and three_of_a_kind(P2) == 0:
								print P1, P2, 'Player 1 wins with three of a kind'
								P1_hands += 1
							elif three_of_a_kind(P2) == 1 and three_of_a_kind(P1) == 0:
								print P1, P2, 'Player 2 wins with three of a kind'
								P2_hands += 1
							elif three_of_a_kind(P1) == 1 and three_of_a_kind(P2) == 1:
									P1pts = 0
									P2pts = 0
									P1s_hand = "".join(map(str, P1))
									P2s_hand = "".join(map(str, P2))
									for value in values:
										if P1s_hand.count(value) == 3:
											P1pts = values.index(value)
										if P2s_hand.count(value) == 3:
											P2pts = values.index(value)
									if P1pts > P2pts:
										P1_hands += 1
									elif P2pts > P1pts:
										P2_hands += 1
									else:
										print P1, P2, 'tie'
							elif three_of_a_kind(P1) == 0 and three_of_a_kind(P2) == 0:
								if two_pairs(P1) == 1 and two_pairs(P2) == 0:
									print P1, P2, 'Player 1 wins with two pairs'
									P1_hands += 1
								elif two_pairs(P2) == 1 and two_pairs(P1) == 0:
									print P1, P2, 'Player 2 wins with two pairs'
									P2_hands += 1
								elif two_pairs(P1) == 0 and two_pairs(P2) == 0:
									if one_pair(P1) == 1 and one_pair(P2) == 0:
										print P1, P2, 'Player 1 wins with a pair'
										P1_hands += 1
									elif one_pair(P2) == 1 and one_pair(P1) == 0:
										print P1, P2, 'Player 2 wins with a pair'
										P2_hands += 1
									elif one_pair(P1) == 1 and one_pair(P2) == 1:
										P1pts = 0
										P2pts = 0
										P1s_hand = "".join(map(str, P1))
										P2s_hand = "".join(map(str, P2))
										for value in values:
											if P1s_hand.count(value) == 2:
												P1pts = values.index(value)
											if P2s_hand.count(value) == 2:
												P2pts = values.index(value)
										if P1pts > P2pts:
											P1_hands += 1
										elif P2pts > P1pts:
											P2_hands += 1
										else:
											print '\n', P1, P2, 'tie \n'
									elif one_pair(P1) == 0 and one_pair(P2) == 0:
										if high_card(P1) > high_card(P2):
											print P1, P2, 'Player 1 wins with the high card'
											P1_hands += 1
										else:
											print P1, P2, 'Player 2 wins with the high card'
											P2_hands += 1
print P1_hands, P2_hands
print 'Took', time()-start, 'seconds'