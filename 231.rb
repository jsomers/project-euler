class Integer
  def primes
    # cf. http://snippets.dzone.com/posts/show/3734
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
end

def ct(n)
  ct = 0
  n.primes.each do |p|
    x = n / p
    while x > 0
      ct += p * x
      x = x / p
    end
  end
  return ct
end

p ct(20_000_000) - ct(15_000_000) - ct(5_000_000)
# takes 38 seconds.