# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

numbers = range(1, 101)
squares = [x**2 for x in numbers]
print "answer =", sum(numbers)**2 - sum(squares)
