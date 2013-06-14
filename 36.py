# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

def bin(n, l): # don't initiate list in here (do it in the function call)
    if n == 0:
        done = "".join(map(str, l)) # concatenate list elements into string
        return done
    elif n % 2 == 0 and n != 0:
        l.insert(0, 0)	# prepend the list
        return bin(n/2, l)	# don't forget to return values for everything
    elif n % 2 != 0 and n != 0:
        l.insert(0, 1)
        return bin((n-1)/2, l)

def palindrome(s):
    rev = s[::-1]
    if s == rev:
        return True
    else:
        return False

trues = []

for i in range(1, 1000000, 2): # check odds only (evens will be "1 .. 0" in binary)
    if palindrome(str(i)) == True and palindrome(bin(i, [])) == True:
        trues.append(i)
print trues, sum(trues)