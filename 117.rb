class Array
  def sum
    return self.inject {|sum, n| sum += n}
  end
  def prod
    return self.inject {|pr, n| pr *= n}
  end
end

def fact(n)
  if n == 0 then return 1 end
  return (1..n).to_a.inject {|prod, n| prod *= n}
end

def ncr(n, r)
  return fact(n) / (fact(n - r) * fact(r))
end

def ct(lst)
  k, m = lst.length, 50 - lst.sum
  return ncr(k + m, k) * combutations(lst)
end

def combutations(lst)
  return fact(lst.length) / lst.uniq.collect {|x| fact(lst.length - (lst - [x]).length)}.prod
end

total = 0
# 2s alone:
(1..25).each {|k| total += ct([2] * k)}
# 3s alone:
(1..16).each {|k| total += ct([3] * k)}
# 4s alone:
(1..12).each {|k| total += ct([4] * k)}

# 2s & 3s:
(1..23).each do |i|
  x = (50 - 2 * i) / 3
  (1..x).each do |j|
    ls = [2] * i + [3] * j
    total += ct(ls)
  end
end
# 2s & 4s:
(1..23).each do |i|
  x = (50 - 2 * i) / 4
  (1..x).each do |j|
    ls = [2] * i + [4] * j
    total += ct(ls)
  end
end
# 3s & 4s:
(1..15).each do |i|
  x = (50 - 3 * i) / 4
  (1..x).each do |j|
    ls = [3] * i + [4] * j
    total += ct(ls)
  end
end

# 2s & 3s & 4s:
(1..21).each do |i|
  x = (50 - 2 * i - 4) / 3
  (1..x).each do |j|
    y = (50 - 2 * i - 3 * j) / 4
    (1..y).each do |k|
      ls = [2] * i + [3] * j + [4] * k
      total += ct(ls)
    end
  end
end
p total