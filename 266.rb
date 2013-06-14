def fact(n)
  if n == 0 then return 1 end
  return (1..n).to_a.inject {|pr, a| pr *= a}
end

def ncr(n, r)
  return fact(n) / (fact(n - r) * fact(r))
end

class Array
  def prod
    return self.inject{|pr, a| pr *= a}
  end
end

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181]
p = PRIMES.prod
SQRT = Math::sqrt(p)

# Any selection 26 elements or larger is too big.
# The product of the largest 16 elements is too small.
LRGST = 2323178904180470194194849106269260585

def up(lst, i=lst.length - 1)
  while true
    cp = lst.clone
    p = lst[i]
    pi = PRIMES.index(p)
    next_p = PRIMES[pi + 1]
    if next_p.nil? or lst[i + 1] == next_p
      i -= 1
    else
      lst[i] = next_p
      if lst.prod > SQRT
        return cp
      end
    end
  end
end

def down(lst)
  i = lst.length - 1
  while true
    p = lst[i]
    pi = PRIMES.index(p)
    prev_p = PRIMES[pi - 1]
    lst[i] = prev_p
    if lst[i] == lst[i - 1]
      i -= 1
    else
      return [lst, i - 1]
    end
  end
end

lst = PRIMES[0..23]

def run(lst)
  lrgst = nil
  i = lst.length - 1
  min_i = i
  while true
    if i > min_i
      break
    end
    min_i = i
    lst = up(lst, i)
    if lst.prod >= LRGST
      puts "LARGEST FOUND"
      p lst
      puts lst.prod
      lrgst = lst.prod
    end
    ret = down(lst)
    lst = ret[0]
    i = ret[1]
  end
  return lrgst
end

lrgst = LRGST
(0..25).each do |j|
  lst = PRIMES[j..j + 22]
  if lst.prod <= SQRT
    lrgst = run(lst)
  end
end
