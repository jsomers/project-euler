import time
import math
from DecInt import DecInt

M43 = 30402457
M42 = 25964951
M41 = 24036583

expt = M43

# DecInt supports an optional value that specifies how many digits
# per term should be used in calculations. The best running time is
# when there are 8192 terms in the final result.

howmany = math.ceil(expt * math.log10(2) / 8192)

print "Calculating 2^%s" % expt

start = time.time()
bignum = DecInt(2, howmany) ** expt - 1
etime = time.time() - start
print "Exponentiation time: %5.3f" % etime

start = time.time()
bigstr = str(bignum)
dtime = time.time() - start
print "Conversion to decimal format: %5.3f" % dtime

print "Total elapsed time: %5.3f" % (dtime + etime)

print "Length of result: %s digits" % len(bigstr)
