class Integer
  def primes   # cf. http://snippets.dzone.com/posts/show/3734
     sieve = []
     3.step(self, 2) { |i| sieve[i] = i }
     sieve[1] = nil
     sieve[2] = 2
     3.step(Math.sqrt(self).floor, 2) do |i| 
        next unless sieve[i]
        (i*i).step(self, i) do |j|
           sieve[j] = nil
        end
     end
     sieve.compact!
  end
  def primes2       # cf. http://snippets.dzone.com/posts/show/3734
    primes = [nil, nil].concat((2..self).to_a)
    (2 .. Math.sqrt(self)).each do |i|
      next unless primes[i]
      (i*i).step(self, i) do |j|
        primes[j] = nil
      end
    end
    primes.compact!
  end
end

def abs(x)
  if x < 0 then -1 * x else x end
end

def is_whole(x)
  return (x - x.to_i) < 10 ** -8 || (1 - (x - x.to_i)) < 10 ** -8
end

def search(p)
  n = 1
  while n < 10**5
    x = (n**3 + n**2 * p)
    if is_whole(x ** (1/3.0))
      return [p, n, x]
    end
    n += 1
  end
  return false
end

# "Cuban primes":
primes = 1_000_000.primes
(1..10_000).each do |s|
  n = s**3
  the_p = 0
  primes.each do |p|
    x = (s**9 + s**6 * p)
    if is_whole(x**(1/3.0))
      t = [x, n, p]
      p t
      the_p = p
    end
  end
  if !(the_p == 0)
    primes = primes[primes.index(the_p)..-1]
  end
end