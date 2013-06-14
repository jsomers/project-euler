require "memoize"
include Memoize

def ways(m, n)
  result = 0
  (m..n).each do |block|
    (0..n - block).each do |start|
      result += 1
      result += ways(m, n - block - start - 1)
    end
  end
  return result
end

memoize(:ways)
p ways(10, 57) + 1

m = 50

(0..200).each do |n|
  p [n, ways(m, n) + 1]
end