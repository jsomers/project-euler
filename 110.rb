require 'mathn'

list = [3] * 15

def size(list)
  list.inject {|pr, x| pr * x}
end

def check(list)
  size(list) >= 8_000_000
end

def sol(list)
  primes = Prime.new
  list.sort.reverse.unshift(1).inject {|pr, x| pr * primes.next ** ((x - 1) / 2) }
end

def min_inc(list)
  list.sort!
  list[0] += 2
  list
end

def pop(list)
  list.sort!
  list.shift
  list
end
#78496567990020180
#18255015811632600
#9350130049860600
      # 1  2  3  4  5  6  7  8  9  0  1  2
p sol([3, 3, 3, 3, 3, 3, 3, 3, 7, 7, 5, 5])


#while check(list)
#  list = pop(list)
#  while not check(list)
#    list = min_inc(list)
#  end
#  p list
#end

#p sol([5, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5])
#
# Rules:
# => Pop a 3 from the list to decrease.
# => Increment one of the guys by 2 to increase.
# => The bigger your guy, the less the increment increases.
# => Try to keep the spread as diffuse as possible (i.e., prefer low increments).