# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

print abs(sum([n ** 2 for n in range(1, 101)]) - sum(range(1, 101)) ** 2)