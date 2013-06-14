def tilings(bs, ts):
    ways = [1]
    for s in range(1, bs + 1):
        print ways[-1]
        ways.append(sum([ways[s - size] for size in ts + [1] if s >= size]))
    return ways[bs]
 
print tilings(50, [2,3,4])