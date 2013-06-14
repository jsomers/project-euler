# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# one (3) two (3) three (5) four (4) five (4) six (3) seven (5) eight (5) nine (4) ten (3)
# eleven (6) twelve (6) thirteen (8) fourteen (8) fifteen (7) sixteen (7) seventeen (9) eighteen (8) nineteen (8)
# twenty (6) thirty (6) forty (5) fifty (5) sixty (5) seventy (7) eighty (6) ninety (6) hundred (7)
# thousand (8)
# and (3)

total = 0
# 1 - 10:
total += 36 + 3
# 11 - 19:
total += 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8
# 20 - 29:
total += 36 + 6*10
# 30 - 39:
total += 36 + 6*10
# 40 - 49:
total += 36 + 5*10
# 50 - 59:
total += 36 + 5*10
# 60 - 69:
total += 36 + 5*10
# 70 - 79:
total += 36 + 7*10
# 80 - 89:
total += 36 + 6*10
# 90 - 99:
total += 36 + 6*10

# 100 - 199
total += 10 + 13*99 + 854
# 200 - 299
total += 10 + 13*99 + 854
# 300 - 399
total += 12 + 15*99 + 854
# 400 - 499
total += 11 + 14*99 + 854
# 500 - 599
total += 11 + 14*99 + 854
# 600 - 699
total += 10 + 13*99 + 854
# 700 - 799
total += 12 + 15*99 + 854
# 800 - 899
total += 12 + 15*99 + 854
# 900 - 999
total += 11 + 14*99 + 854 

# 1000
total += 11

print total