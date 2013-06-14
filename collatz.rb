index = {}

def nxt(n)
  (n % 2 == 0 ? n / 2 : 3 * n + 1)
end

(2..1_000_000).each do |n|
  c = n + 0
  ct = 0
  while n > 1
    if index[n] then ct += index[n]; break end
    n = nxt(n)
    ct += 1
  end
  index[c] = ct
end

p index.sort {|a, b| b[1] <=> a[1]}.first[0]