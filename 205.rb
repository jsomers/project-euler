peter_sums = {}
peter_roll = [1, 1, 1, 1, 1, 1, 1, 1, 1]

colin_sums = {}
colin_roll = [1, 1, 1, 1, 1, 1]

def next_roll(roll, n)
  i = -1
  chg = false
  while not chg
    if roll[i] != n
      roll[i] += 1
      chg = true
    else
      roll[i] = 1
      i -= 1
    end
  end
  return roll
end

class Array
  def sum
    return self.inject {|sum, n| sum + n}
  end
end

while peter_roll != [4, 4, 4, 4, 4, 4, 4, 4, 4]
  begin
    peter_sums[peter_roll.sum] += 1
  rescue
    peter_sums[peter_roll.sum] = 1
  end
  peter_roll = next_roll(peter_roll, 4)
end
peter_sums[36] = 1

while colin_roll != [6, 6, 6, 6, 6, 6]
  begin
    colin_sums[colin_roll.sum] += 1
  rescue
    colin_sums[colin_roll.sum] = 1
  end
  colin_roll = next_roll(colin_roll, 6)
end
colin_sums[36] = 1

prob = 0
peter_sums.each do |prs, prc|
  prob_peter_roll = prc / peter_sums.values.sum.to_f
  worse_colin_rolls = colin_sums.select {|crs, crc| crs < prs}
  colin_probs = worse_colin_rolls.collect {|crs, crc| crc / colin_sums.values.sum.to_f}
  peter_win_events = colin_probs.collect {|prob_colin_roll| prob_colin_roll.to_f * prob_peter_roll}
  prob += peter_win_events.sum
end

puts prob
# PETER DISTRIBUTION:
# 9 => 1
# 10 => 9
# 11 => 45
# 12 => 165
# 13 => 486
# 14 => 1206
# 15 => 2598
# 16 => 4950
# 17 => 8451
# 18 => 13051
# 19 => 18351
# 20 => 23607
# 21 => 27876
# 22 => 30276
# 23 => 30276
# 24 => 27876
# 25 => 23607
# 26 => 18351
# 27 => 13051
# 28 => 8451
# 29 => 4950
# 30 => 2598
# 31 => 1206
# 32 => 486
# 33 => 165
# 34 => 45
# 35 => 9
# 36 => 1
# Outcomes: 1, 9, 45, 165, 486, 1206, 2598, 4950, 8451, 13051, 18351, 23607, 27876, 30276, 30276, 27876, 23607, 18351, 13051, 8451, 4950, 2598, 1206, 486, 165, 45, 9, 1
# Total: 262144

# COLIN DISTRIBUTION:
# 6 => 1
# 7 => 6
# 8 => 21
# 9 => 56
# 10 => 126
# 11 => 252
# 12 => 456
# 13 => 756
# 14 => 1161
# 15 => 1666
# 16 => 2247
# 17 => 2856
# 18 => 3431
# 19 => 3906
# 20 => 4221
# 21 => 4332
# 22 => 4221
# 23 => 3906
# 24 => 3431
# 25 => 2856
# 26 => 2247
# 27 => 1666
# 28 => 1161
# 29 => 756
# 30 => 456
# 31 => 252
# 32 => 126
# 33 => 56
# 34 => 21
# 35 => 6
# 36 => 1
# Outcomes: 1, 6, 21, 56, 126, 252, 456, 756, 1161, 1666, 2247, 2856, 3431, 3906, 4221, 4332, 4221, 3906, 3431, 2856, 2247, 1666, 1161, 756, 456, 252, 126, 56, 21, 6, 1
# Total: 46656