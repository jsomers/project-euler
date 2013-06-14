def T(n)
  return n * (n + 1) / 2
end

def tiles_in_wrapping(a, n)
  return (n + 1) * a + T(n) * 8
end

def even_factor_pairs(n)
  return (1..Math::sqrt(n).to_i / 2).collect {|i| i * 2}.select {|a| n % a == 0}.collect {|a| [a, n / a]}.reject {|x| x[0] % 2 == 1 or x[1] % 2 == 1 or x[0] == x[1]}
end

ct = 0
(1..500000).collect {|i| i * 2}.each do |n|
  ct += even_factor_pairs(n).length
end
p ct

#ct = 0
#(1..10).each do |s|
#  p s**2
#  a = (s % 2 == 0 ? s**2 + 8 : s**2 + 7)
#  n = 0
#  while (tiw = tiles_in_wrapping(a, n)) <= 10**2
#    puts "> #{tiw}"
#    ct += 1
#    n += 1
#  end
#end
#p ct