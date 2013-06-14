primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def fact(n)
  if n == 0 then return 1 end
  return (1..n).to_a.inject {|pr, a| pr *= a}
end

def ncr(n, r)
  return fact(n) / (fact(n - r) * fact(r))
end

class Array
  def prod
    return self.inject {|pr, a| pr *= a}
  end
end

puts Math::log(10**9 * Math::sqrt(primes.prod))**primes.length / (fact(primes.length) * Math::log(2) * Math::log(3) * Math::log(5) * Math::log(7) * Math::log(11) * Math::log(13) * Math::log(17) * Math::log(19) * Math::log(23) * Math::log(29) * Math::log(31) * Math::log(37) * Math::log(41) * Math::log(43) * Math::log(47) * Math::log(53) * Math::log(59) * Math::log(61) * Math::log(67) * Math::log(71) * Math::log(73) * Math::log(79) * Math::log(83) * Math::log(89) * Math::log(97))
# 30129530