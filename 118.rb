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
end

class Array
  def filter(n)
    used = n.to_s.split("")
    return self.select {|m| m > n && (m.to_s.split("") & used).empty?}
  end
end

primes = 10_000_000.primes.reject {|p| l = p.to_s.split(""); l.uniq.length < l.length}
# [13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
primes = primes.filter(13)
#p primes.filter(23).first

#p [primes.length, primes.filter(23).length]

p primes.select {|p| p > 10**6}

#p sprimes.select {|p|  primes.filter(p).length > 0}