require 'prime'
require 'combinatorics'

# ======== TABLE OF RESULTS =================
#  d | M(10, d) |  N(10, d) |    S(10, d)        
# ===========================================
# 0 #     8    #    8      #   38000000042   
# 1 #     9    #    11     #   12882626601       
# 2 #     8    #    39     #   97447914665        
# 3 #     9    #    7      #   23234122821        
# 4 #     9    #    1      #   4444444447      
# 5 #     9    #    1      #   5555555557        
# 6 #     9    #    1      #   6666666661      
# 7 #     9    #    7      #   59950904793     
# 8 #     8    #    32     #   285769942206      
# 9 #     9    #    8      #   78455389922      
# ===========================================

def pad_with_zeros(s, n)
  '0' * (n - s.length) + s
end

def others(n_spots, outlaw)
  max = 10 ** n_spots
  (0..max - 1).each do |x|
    str_x = pad_with_zeros(x.to_s, n_spots)
    if not str_x.index(outlaw.to_s)
      yield str_x.split("").collect {|d| d.to_i}
    end
  end
end

def cycle(k, fill_digit)
  sols = []
  (0..9).to_a.comb(k) do |index_set|
    n = [0] * 10
    index_set.each {|i| n[i] = fill_digit}
    free_spots = (0..9).to_a - index_set
    others(10 - k, fill_digit) do |other|
      free_spots.zip(other).each {|i, x| n[i] = x}
      if (s = n.join("").to_i) >= 10 ** 9 and s.prime?
        sols << s
      end
    end
  end
  sols
end

sol = cycle(9, 9)
p [sol.length, sol.sum, sol]

#p [38000000042, 12882626601, 97447914665, 23234122821, 4444444447, 5555555557, 6666666661, 59950904793, 285769942206, 78455389922].sum