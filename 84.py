from random import *

board = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3', 'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3', 'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'U2', 'F3', 'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']
lands = [0]*41

position = [0]*100002
print 'After 100,000 rolls...'
def roll():
	return randint(1, 5), randint(1, 5)

for move in range(100000):
	if board[position[move]].count('CH') > 0:
		draw = randint(1, 16)
		if draw == 1:
			position[move+1] = 0 # go to GO next turn
		elif draw == 2:
			position[move+1] = 10 # JAIL
		elif draw == 3:
			position[move+1] = 11 # C1
		elif draw == 4:
			position[move+1] = 24 # E3
		elif draw == 5:
			position[move+1] = 40 # H2
		elif draw == 6:
			position[move+1] = 5 # R1
		elif draw == 7 or draw == 8:
			me = position[move]
			for square in range(me, 200):
				if board[square % 41].count('R') > 0:
					position[move+1] = square % 41 # the nearest railroad!
					break
		elif draw == 9:
			me = position[move]
			for square in range(me, 200):
				if board[square % 41].count('U') > 0:
					position[move+1] = square % 41 # the nearest utility
					break
		elif draw == 10:
			position[move+1] = (position[move] - 3) % 41
		else:
			lands[position[move]] += 1
			the_roll = roll()
			position[move+1] = (position[move] + sum([the_roll[0], the_roll[1]])) % 41
	elif board[position[move]].count('CC') > 0:
		draw = randint(1, 16)
		if draw == 1:
			position[move+1] = 0
		elif draw == 2:
			position[move+1] = 10
		else:
			lands[position[move]] += 1
			the_roll = roll()
			position[move+1] = (position[move] + sum([the_roll[0], the_roll[1]])) % 41
	elif board[position[move]].count('G2J') > 0:
		position[move+1] = 10
	else:
		lands[position[move]] += 1
		the_roll = roll()
		position[move+1] = (position[move] + sum([the_roll[0], the_roll[1]])) % 41

a = board[lands.index(max(lands))]
lands.remove(max(lands))
b = board[lands.index(max(lands))+1]
lands.remove(max(lands))
c = board[lands.index(max(lands))+2]

print 'simulation:', a, b, c
print 'actual:', board[10], board[15], board[24]