class Array
  def sum
    inject( nil ) { |sum,x| sum ? sum + x : x }
  end
  
  def comb(n = size)
    if size < n or n < 0
    elsif n == 0
      yield([])
    else
      self[1..-1].comb(n) do |x|
	yield(x)
      end
      self[1..-1].comb(n - 1) do |x|
	yield([first] + x)
      end
    end
  end
  
  def perm(n = size)
    if size < n or n < 0
    elsif n == 0
      yield([])
    else
      self[1..-1].perm(n - 1) do |x|
	(0...n).each do |i|
	  yield(x[0...i] + [first] + x[i..-1])
	end
      end
      self[1..-1].perm(n) do |x|
	yield(x)
      end
    end
  end
end

if $0 == __FILE__
  ["a", "b", "c", "d"].comb(3) do |x|
    p x
  end
end