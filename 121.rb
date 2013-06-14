N = 15

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

def indices(array, r)
  n = array.length
  indices = (0...r).to_a
  final = (n - r...n).to_a
  while indices != final
    yield indices.map {|k| array[k]}
    i = r - 1
    while indices[i] == n - r + i
      i -= 1
    end
    indices[i] += 1
    (i + 1...r).each do |j|
      indices[j] = indices[i] + j - i
    end
  end
  yield indices.map {|k| array[k]}
end

def combos(r)
  combos = []
  indices((0..N - 1).to_a, r) do |is|
    a = [0] * N
    is.each {|i| a[i] = 1}
    combos << a
  end
  return combos
end

def productize(lst)
  pr = 1
  lst.each_with_index do |a, i|
    if a == 0
      pr *= (i + 1)
    end
  end
  return pr
end

s = 0
(N/2 + 1..N).each do |bs|
  s += combos(bs).collect {|c| productize(c)}.sum
end
frac = [s, fact(N + 1)]
up = frac[1] - frac[0]
dwn = -1 * frac[0]
(1..5000).each do |i| 
  if up + i * dwn < 0
    p i
    break
  end
end