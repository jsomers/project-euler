def tetration(n, r)
  if r == 1
    return n
  end
  return n ** tetration(n, r - 1)
end

def mod_tetration(n, r)
  if r == 1
    return n % 10**5
  end
  return (n % 10**5) ** tetration(n, r - 1)
end

def iterLog(n)
  i = 0
  while n > 1
    n = Math::log(n)
    i += 1
  end
  return i
end

def cycle(d)
  ns = []
  i = 1
  while true
    x = 1777**i % 10**d
    if !ns.include? x
      ns << x
    else
      return ns.collect {|n| n / 10**(d - 1)}
    end
    i += 1
  end
end

def easy_cycle(d)
  ns = []
  i = 1
  while true
    x = 777**i % 10**d
    if !ns.include? x
      ns << x
    else
      return ns.collect {|n| n / 10**(d - 1)}
    end
    i += 1
  end
end

#p tetration(3, 3)

def order(a, m)
  b, e = a % m, 1
  while (b != 1)
    b = (a * b) % m
    e += 1
  end
  e
end
 
def mexp(a, e, m)
  r, b, k = 1, a, e
  while (k > 0)
    r = (r * b) % m if k & 1 == 1
    k >>= 1
    b = (b * b) % m
    return 0 if b == 0
    return r if b == 1
  end
  r
end
 
def mtet(a, t, m)
  return 0 if m == 1
  return a % m if t == 1
  ord = order(a, m)
  e = mtet(a, t - 1, ord)
  mexp(a, e, m)
end
 
puts mtet(1777, 1855, 100_000_000)