#!/usr/bin/ruby

def double(lod)
  (lod2 = lod.map {|d| d * 2}).each_with_index do |d, i|
    if d >= 10
      lod2[i] = d - 10
      if i == lod2.length - 1 # over
        lod2.push(1)
      else
        lod2[i + 1] = lod2[i + 1] + 1
      end
    end
  end
  lod2
end

l = list_of_digits = [1]; 1000.times { l = double(l) }

p l.inject(0) {|s, a| s += a}