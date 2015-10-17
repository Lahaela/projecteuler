import random
def isPrime(number):
    for x in range (2,int(number**0.5+1)):
        if (number % x == 0):
            return False
    return True    

def factorial(tralala):
    total = 1
    while tralala > 0:
        total *= tralala
        tralala -= 1
    return total
    
def counts(options):
    count = []
    for p in options:
        if p not in count:
            count.append(p)
    return count
    
def rotation(lala):
    global primes
    options = []
    for char in range(0,len(lala)):
        options.append(lala[char])
    count = counts(options) # factorial is only of unique elements, but options must contain everything
    if ('0' in count) or ('2' in count) or ('4' in count) or ('6' in count) or ('8' in count) or ('5' in count):
        return False
    results = []
    while len(results) < factorial(len(count)):
        m = options[:]
        z = random.choice(m)
        m.remove(z)
        while len(z) < len(options):
            y = random.choice(m)
            m.remove(y)
            z += y
        if int(z) not in primes: # might be faster if primes is generated all at once, rather than repeated testing
            return False
        if z not in results:
            results.append(z)
    for finalcheck in results:
        if int(finalcheck) not in primes:
            return False
    return True
    
res = [2,5]
primes = [1,2,3]
for n in range(5,1000000,2):
    if isPrime(n):
        primes.append(n)
for e in primes:        
    if rotation(str(e)):
        res.append(e)
        
print len(res)-1
print res