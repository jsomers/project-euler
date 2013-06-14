import math  
  
def isPrime(n):     
    if (n==1):     
        return False    
    if (n==2):     
        return True    
    sqrt_n = math.sqrt(n)     
    i = 2    
    flag = True    
    while i <= sqrt_n:     
        if (n%i) == 0:     
            flag = False    
            break    
        i += 1    
    return flag     
    
def getPrimeList(limit):     
    l = []  
    i = 2  
    while i <= limit:     
        if isPrime(i):     
            l.append(i)     
        i += 1    
    return l  
  
def HammingNumber(n, l, limit, dept):  
    result = 0  
  
    for i in xrange(len(l)):  
        if n*l[i] > limit:  
            break  
          
        result += 1  
        result += HammingNumber(n*l[i], l[i:], limit, dept+1)  
          
    return result  
  
def test():  
    hamming_number = 100  
    limit = pow(10, 9)  
    l = getPrimeList(hamming_number)  
    result = HammingNumber(1, l, limit, 1) + 1  
    print 'Answer #204 : %s' % result  
    pass

test()