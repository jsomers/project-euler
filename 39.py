# If p is the perimeter of a right angle triangle, {a, b, c}, which value, for p <= 1000, has the most solutions?
# generate triplets using 3,4,5; 5, 12, 13; 8, 15, 17; 7, 24, 25; 15, 112, 113

trips = []
for i in range(100):
	a = 3*i
	b = 4*i
	c = 5*i
	if [a, b, c] not in trips and a+b+c < 1001:
		trips.append([a, b, c])

for i in range(100):
	a = 5*i
	b = 12*i
	c = 13*i
	if [a, b, c] not in trips  and a+b+c < 1001:
		trips.append([a, b, c])

for i in range(100):
	a = 8*i
	b = 15*i
	c = 17*i
	if [a, b, c] not in trips  and a+b+c < 1001:
		trips.append([a, b, c])

for i in range(100):
	a = 7*i
	b = 24*i
	c = 25*i
	if [a, b, c] not in trips  and a+b+c < 1001:
		trips.append([a, b, c])
		
for i in range(100):
	a = 15*i
	b = 112*i
	c = 113*i
	if [a, b, c] not in trips  and a+b+c < 1001:
		trips.append([a, b, c])

for i in range(0, 1000):
	for trip in trips:
		if sum(trip) == i:
			print trip, sum(trip)