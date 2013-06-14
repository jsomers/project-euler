def factors(n)
  return (1..n).select {|x| n % x == 0}
end

def factorize(orig)
    factors = {}
    factors.default = 0     # return 0 instead nil if key not found in hash
    n = orig
    i = 2
    sqi = 4                 # square of i
    while sqi <= n do
        while n.modulo(i) == 0 do
            n /= i
            factors[i] += 1
            # puts "Found factor #{i}"
        end
        # we take advantage of the fact that (i +1)**2 = i**2 + 2*i +1
        sqi += 2 * i + 1
        i += 1
    end
    
    if (n != 1) && (n != orig)
        factors[n] += 1
    end
    factors
end

def fact(n)
  if n == 0 then return 1 end
  return (1..n).to_a.inject {|pr, a| pr *= a}
end

def ncr(n, r)
  return fact(n) / (fact(n - r) * fact(r))
end

class Array
  def sum
    return self.inject {|sum, a| sum += a}
  end
end

pascals = []
(1..50).each do |n|
  (0..n - 1).each do |i|
    pascals << ncr(n, i)
  end
end

p pascals.uniq.select {|n| (x = factorize(n).values.max).nil? or x == 1}.sum