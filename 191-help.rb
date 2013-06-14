class String
  def count(letter)
    a = self.split("")
    return a.length - (a - [letter]).length
  end
end

def step(lst)
  i = lst.length - 1
  while i >= 0
    if lst[i] < 2
      lst[i] += 1
      return lst
    else
      lst[i] = 0
      i -= 1
    end
  end
  return lst
end

def to_string(lst)
  map = {0 => "O", 1 => "A", 2 => "L"}
  return lst.collect {|x| map[x]}.join("")
end

n = 4
lst = [0] * n
ct = 0
zero_ls = 0
one_l_end_with_aa = 0
(0..3**n - 1).each do |i|
  lst = step(lst)
  s = to_string(lst)
  if !s.include? "AAA" and s.count("L") < 2
    puts s
    ct += 1
    if s.count("L") == 0
      zero_ls += 1
    end
    if s[-2..-1] == "AA" and s.count("L") == 1
      one_l_end_with_aa += 1
    end
  end
end
p zero_ls
#p one_l_end_with_aa