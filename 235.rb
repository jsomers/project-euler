R = 1.002322108632876
M = -600_000_000_000

def diff(x)
  return (x - M).abs
end

def u(k)
  (900 - 3 * k) * R ** (k - 1)
end

puts u(566).to_f

def s(n)
  (1..n).collect {|k| u(k)}.inject {|a, n| n += a}
end

p s(5000).to_s.reverse.gsub(%r{([0-9]{3}(?=([0-9])))}, "\\1,").reverse
p (s(5000) < M ? "left" : "right")

s=0
# for(k=1,5000, s += ((900 - 3 * k) * r^(k - 1)))