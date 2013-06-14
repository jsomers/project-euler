# [n, tot, -AA, 0Ls, -A, 1L-AA, 1L-A, 1LnotA]
lst = [2, 3, 0, 2, 1, 0, 0, 1]
while lst[0] <= 30
  n, a, b, c, d, e, f, g = lst
  lst = [n + 1, 2 * a + c - b, d, 2 * c - b + e, a - (b + d), f, g, a]
end
p lst[1]