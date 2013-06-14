def in_interval(A, B, x):
	if A <= B:
		a = A
		b = B
	else:
		a = B
		b = A
	if x <= b and x >= a:
		return 1
	else:
		return 0

def intercepts(xa, ya, xb, yb):
	if xa == xb:
		y = 'none'
		if in_interval(ya, yb, 0):
			x = xa
		else:
			x = 'none'
		return (x, y)
	elif ya == yb:
		x = 'none'
		if in_interval(xa, xb, 0):
			y = ya
		else:
			y = 'none'
		return (x, y)
	else:
		m = float((ya - yb))/(xa - xb)
		y_ = ya - (xa*m)
		x_ = float(-y_)/m
		if in_interval(xa, xb, x_):
			x = x_
		else:
			x = 'none'
		if in_interval(ya, yb, y_):
			y = y_
		else:
			y = 'none'
		return (x, y)
		

#pts = [(-175, 41), (-421, -714), (574, -645)]

def origin(pts):
	x_s = intercepts(pts[0][0], pts[0][1], pts[1][0], pts[1][1])[0], intercepts(pts[0][0], pts[0][1], pts[2][0], pts[2][1])[0], intercepts(pts[1][0], pts[1][1], pts[2][0], pts[2][1])[0]
	y_s = intercepts(pts[0][0], pts[0][1], pts[1][0], pts[1][1])[1], intercepts(pts[0][0], pts[0][1], pts[2][0], pts[2][1])[1], intercepts(pts[1][0], pts[1][1], pts[2][0], pts[2][1])[1]
	x_positive, x_negative, y_positive, y_negative = 0, 0, 0, 0
	for x in x_s:
		if x >= 0 and x != 'none':
			x_positive += 1
		if x <= 0 and x != 'none':
			x_negative += 1
	for y in y_s:
		if y >= 0 and y != 'none':
			y_positive += 1
		if y <= 0 and y != 'none':
			y_negative += 1
	if x_positive > 0 and x_negative > 0 and y_positive > 0 and y_negative > 0:
		return 1
	else:
		return 0


f = open('/triangles.txt', 'rU')

raw = []
for line in f:
	raw.append(line.split(','))

points = []
for trip in raw:
	ptset = [(int(trip[0]), int(trip[1])), (int(trip[2]), int(trip[3])), (int(trip[4]), int(trip[5].replace('\n', '')))]
	points.append(ptset)

tot = 0
for pt in points:
	tot += origin(pt)

print tot