# Strategy:
# => Starting with sequences of k=2 squares, iterate from [1^2, 2^2] up until [x^2, y^2].sum exceeds 10^8
# => Increment k
# => Collect palindromes along the way

def is_palindrome(n)
  return n.to_s == n.to_s.reverse
end

class Array
  def sum
    return self.inject {|sum, n| sum += n}
  end

  def sum_of_squares
    return self.collect {|x| x**2}.sum
  end
end

k = 2
l = (1..k).to_a
palindromes = []
while true
  if l.sum_of_squares >= 10**8
    break
  end
  while (sos = l.sum_of_squares) < 10**8
    if is_palindrome(sos) then palindromes << sos end
    l = l.map {|x| x += 1}
  end
  k += 1
  l = (1..k).to_a
end
p palindromes.uniq.sum