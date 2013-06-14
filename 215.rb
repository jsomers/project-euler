# Utility functions.
def fact(n)
  return (1..n).to_a.prod
end

class Array
  def sum
    return self.inject {|a, s| a += s}
  end
  
  def count(e)
    return self.length - (self - [e]).length
  end
end

# 1. Build and collect the possible bricksets.
X = 32
Y = 10

if X % 2 == 0
  l = [2] * (X / 2)
else
  l = [3] + [2] * (X / 2 - 1)
end

bricksets = []
while true
  bricksets << l
  l = l.clone
  i = l.index(2)
  break if i.nil?
  l[i] += 1
  begin l[i + 1] += 1 rescue break end
  l.pop()
  break if l.sum != X
end

# 2. Generate every permutation of the bricksets.
def slide(i, l)
  "[2, 2, 3, 2, 2] => [2, 2, 2, 3, 2]"
  if (i + 1) < l.length
    l[i + 1] = 3
    l[i] = 2
  end
  l
end

def reset(i, l)
  "[2, 2, 3, 3, 2, 2, 3] => [2, 2, 3, 2, 3, 3, 2]"
  remainder = l[i + 1..-1]
  ts_left = remainder.count(3)
  ws_left = remainder.count(2)
  l[0..i] + [3] * ts_left + [2] * ws_left
end

def tick(b)
  "Generate the 'next' permutation for a given brickset."
  if b.rindex(3) == (b.length - 1) and (b.rindex(3) - b.index(3)) == (b.count(3) - 1)
    return false
  elsif (i = b.rindex(3)) != (b.length - 1)
    return slide(i, b)
  else
    i = b[0..i - 1].rindex(3) until (b[i + 1] != 3 and !b[i + 1].nil?)
    slide(i, b)
    reset(i, b)
  end
end

def pbsets(b)
  "Enumerate all the p-bricksets of a given brickset,
  using the tick function."
  if b.count(2) == b.length
    return [b]
  end
  z = b.clone
  ps = [b]
  while b = tick(b)
    x = b.clone
    ps << x
  end
  # This cloning and shifting nonsense is due to a weird bug.
  ps.shift
  ps.unshift(z)
end

pbs = []
bricksets.each {|b| pbsets(b).each {|pb| pbs << pb}}
PBS = pbs.collect {|x| [pbs.index(x), x]}

# 3. Create an index mapping partial x-wise sums to p-bricksets,
# and use that index to create a matrix of mutually compatible
# p-bricksets
def partials(b)
  "Starting from the left, calculate partial sums of a brickset."
  (0..b.length - 2).collect {|i| b[0..i].sum}
end

Index = {}
PBS.each do |pb|
  partials(pb[1]).each {|x| if Index[x] then Index[x] << pb[0] else Index[x] = [pb[0]] end}
end

def compatibles(b)
  incompatibles = []
  partials(b[1]).each {|b| incompatibles += Index[b]}
  (0..PBS.length - 1).to_a - incompatibles
end

compatimap = {}
PBS.each {|pb| compatimap[pb[0]] = compatibles(pb)}

## 4. Explore the tree exhaustively, expanding at each level using
## the compatimap, a process not unlike the expansion of sentences
## in a context-free grammar.
u = {}
PBS.each {|pb| u[pb[0]] = 1}
n = 0
while (n += 1) < Y
  x = {}
  u.keys.each do |k|
    compatimap[k].each do |i|
      if x[i] then x[i] += u[k] else x[i] = u[k] end
    end
  end
  u = x
end
p u.values.sum