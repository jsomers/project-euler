def sum_digits(n)
  return n.to_s.split("").collect {|x| x.to_i}.inject {|sum, n| sum += n}
end

def test(n)
  return Math::log(n) / Math::log(sum_digits(n)) % 1 == 0
end

ct = 1
p (10..10**8).each {|n| if test(n) then p [ct, n]; ct += 1 end}