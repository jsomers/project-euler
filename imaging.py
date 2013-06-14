import Image, ImageDraw
from random import random

im = Image.new('1', (500, 500))

draw = ImageDraw.Draw(im)

points = []
for x in range(500):
	for y in range(500):
		points.append((x, y))

for pt in points:
	a = random()
	if a >= .5:
		draw.point(pt, fill=128)
	else:
		draw.point(pt, fill=0)
del draw

im.save('/users/jsomers/Desktop/snow.png', 'PNG')