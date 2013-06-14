ss, ds, ts = (1..3).collect {|x| (1..20).collect {|i| i * x}}

ct = 0
for b in [50]
  for s in ss
    for s2 in ss
      if (b + s + s2) < 100
        if s == s2
          p [b, s, s2]
          ct += 1
        end
      end
    end
  end
end
#p ct
p [20, 399, 400, 400, 2825, 6819, 7643, 3857, 7999, 4000, 42, 60, 180, 250, 132, 364, 200, 56, 20, 20, 180, 335, 394, 264, 364, 400, 20, 12, 527].inject {|s, i| s += i}