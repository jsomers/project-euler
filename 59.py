# Using a brute force attack, can you decrypt the cipher using XOR encryption?

# chr and ord for moving between Binary and Ascii... use ^ for XOR

# 103, 111, 100

from random import randint

h = open('/users/jsomers/Documents/Work/Project Euler/cipher1.txt', 'r')

g = open('/users/jsomers/Documents/Work/Project Euler/decrypts.txt', 'w')

# 65-90 and 97-122 and 32

# Encrypted ASCII
crypted = []
for i in h.read().split(','):
	crypted.append(int(i))

# Encrypted Text
cyphertext = []
for i in crypted:
	cyphertext.append(chr(i))

print min(crypted), max(crypted)

key1s = []

# Find which keys produce valid ASCII (i.e., letters only)
for key in range(128):
	ct = 0
	for cipher in crypted[0::3]:
		if cipher^key in range(96, 123) or cipher^key in range(65, 90) or cipher^key == 32 or cipher^key==95 or cipher^key==63:
			ct+=1
	if ct > 300:
		print key, ct, len(crypted[0::3])
	if ct == len(crypted[0::3]):
		print key, 'supposedly works for everything'
		key1s.append(key)

print set(key1s)

key2s = []

for key in range(128):
	ct = 0
	for cipher in crypted[1::3]:
		if cipher^key in range(96, 123) or cipher^key in range(65, 90) or cipher^key == 32 or cipher^key==95 or cipher^key==63:
			ct+=1
	if ct > 300:
		print key, ct, len(crypted[1::3])
	if ct == len(crypted[1::3]):
		print key, 'supposedly works for everything'
		key2s.append(key)

print set(key2s)

key3s = []

for key in range(128):
	ct = 0
	for cipher in crypted[2::3]:
		if cipher^key in range(96, 123) or cipher^key in range(65, 90) or cipher^key == 32 or cipher^key==95 or cipher^key==63:
			ct+=1
	if ct > 300:
		print key, ct, len(crypted[2::3])
	if ct == len(crypted[2::3]):
		print key, 'supposedly works for everything'
		key3s.append(key)

print set(key3s)

def decrypt(L, key1, key2, key3):
	for index in range(len(L)):
		if index % 3. == 0:
			g.write(chr(L[index] ^ key1))
		if index % 3. == 1:
			g.write(chr(L[index] ^ key2))
		if index % 3. == 2:
			g.write(chr(L[index] ^ key3))
	return
# for key1 in set(key1s):
# 	for key2 in set(key2s):
# 		for key3 in set(key3s):
decrypt(crypted, 103, 111, 100)

tot = 0

for item in crypted[::3]:
	tot+=item^103
for item in crypted[1::3]:
	tot+=item^111
for item in crypted[2::3]:
	tot+=item^100

print tot