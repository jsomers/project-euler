a, c, xm = 0, 250_000, 500
(1..xm).each do |x|
  #a += c / x
  #p a - xm * (xm + 1) / 2
end

# t = b^2 - a^2
ts = Hash.new(0)
a = 1
b = a + 2
(1..10).each do |a|
  b = a + 2
  while b < 10 && (tc = b**2 - a**2) <= 10**6
    ts[tc] += 1
    b += 2
  end
end
p ts.select {|t, ways| t == 32}