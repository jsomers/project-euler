# Find the last ten digits of: 28433 x 2^7830457 + 1
from math import log

x = 28433 * 2**7830457 + 1
y = 123459438294734
print x % 10**10