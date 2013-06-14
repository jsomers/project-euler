def remainder(a, n)
  return ((a - 1)**n + (a + 1)**n) % a**2
end

class Array
  def sum
    return self.inject {|sum, a| sum += a}
  end
end

max_remainders = []
(3..1000).each do |a|
  remainders = []
  (1..500).collect {|n| 2 * a * n}.each {|x| remainders << x % a**2}
  max_remainders << remainders.uniq.max
end

p max_remainders.sum
# 333082500