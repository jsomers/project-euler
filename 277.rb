SEQ = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
def seq(n)
  seq = ""
  i = 0
  while n != 1
    if n % 3 == 0
      n = n / 3
      seq += "D"
    elsif n % 3 == 1
      n = (4 * n + 2) / 3
      seq += "U"
    else
      n = (2 * n - 1) / 3
      seq += "d"
    end
    if seq != SEQ[0..i]
      break
    end
    i += 1
  end
  return seq[0..-2]
end

#p seq(1004064)
n = 10**15 + 3967833364518
while true
  p [n, seq(n), SEQ.length - seq(n).length]
  n += 7625597484987
end