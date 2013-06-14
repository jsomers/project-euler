require "memoize"
include Memoize

def add_pairwise(l1, l2)
  return [l1[0] + l1[1], l2[0] + l2[1]]
end

def steps(n)
  if n == 1
    return [[1, 0]]
  elsif n == 2
    return [[1, 1]]
  else
    candidates = []
    (1..n/2).each do |i|
      s_i = steps(i)
      s_n_i = steps(n - i)
      cand = s_i | s_n_i
      cand += [add_pairwise(s_i[-1], s_n_i[-1])]
      candidates << [cand.reject {|x| x == [1, 0]}.length, cand]
    end
    return candidates.sort.first[1]
  end
end

def multi_steps(n)
  if n == 1
    return [[[1, 0]]]
  elsif n == 2
    return [[[1, 1]]]
  else
    candidates = []
    (1..n/2).each do |i|
      multi_steps(i).each do |s_i|
        multi_steps(n - i).each do |s_n_i|
          cand = s_i | s_n_i
          cand += [add_pairwise(s_i[-1], s_n_i[-1])]
          candidates << [cand.reject {|x| x == [1, 0]}.length, cand]
        end
      end
    end
    #p candidates
    all = candidates.select {|c| c[0] == candidates.sort.first[0]}
    #return candidates.sort.first[1]
    return all.collect {|a| a[1]}
  end
end
# The fastest way for m > n does not always use the fastest way for n.
# => In the case of m=15, you want the way for n=6 that uses 3, so that
# => later you can do 12 + 3.

memoize(:multi_steps)
#p multi_steps(120).first.reject {|step| step == [1, 0]}.length
#sum = 0
#(1..200).each do |n|
#  sum += multi_steps(n).first.reject {|step| step == [1, 0]}.length
#  p [n, multi_steps(n).first.reject {|step| step == [1, 0]}.length]
#end
#p sum
# TODO: If there are many equally good guys, make sure to try them all!
memoize(:steps)
p steps(120).reject {|step| step == [1, 0]}.length
#sum = 0
#(1..200).each do |n|
#  sum += steps(n).reject {|step| step == [1, 0]}.length
#  p [n, steps(n).reject {|step| step == [1, 0]}.length]
#end
#p sum

# Ideas:
# => go with the approximation (1620). Search around it.
# => try a low sequence and check OEIS.
# => figure out some fast non-recursive method for a given n.
# => use the recursive method, but allow the top *2* candidates, not just the one.