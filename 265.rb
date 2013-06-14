N = 5

def dec2bin(n)
  [n].pack("N").unpack("B32")[0].sub(/^0+(?=\d)/, '')
end

def bin2dec(n)
  [("0"*32+n.to_s)[-32..-1]].pack("B32").unpack("N")[0]
end

class Array
  def sum
    return self.inject {|sum, a| sum += a}
  end
end

candidates = [{:seq => [0] * N, :used => ["0" * N]}]

def step(candidates)
  noobs = []
  candidates.each do |leaf|
    one = leaf[:seq] + [1]
    zero = leaf[:seq] + [0]
    if !leaf[:used].include?(one_s = one[-N..-1].to_s)
      if one.length < 2**N or (one.length == 2**N && !leaf[:used].include?(one_s = ([one[-1]] + one[0..N - 2]).to_s))
        noobs << {:seq => one, :used => leaf[:used] + [one_s]}
      end
    end
    if !leaf[:used].include?(zero_s = zero[-N..-1].to_s)
      if zero.length < 2**N or (zero.length == 2**N && !leaf[:used].include?(zero_s = ([zero[-1]] + zero[0..N - 2]).to_s))
        noobs << {:seq => zero, :used => leaf[:used] + [zero_s]}
      end
    end
  end
  return noobs
end

i = 1
while i <= 27
  candidates = step(candidates)
  i += 1
end
p candidates.collect {|c| bin2dec(c[:seq].to_s.to_i)}.sum