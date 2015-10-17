
def isPrime(number):
    for x in range (2,int(number**0.5+1)):
        if (number % x == 0):
            return False
    return True    
    
def rotation(lala):
    global primes
    options = []
    for char in range(0,len(lala)):
        options.append(lala[char])
    results = []
    while len(results) < len(lala):
        options.append(options.pop(0))
        z = ''
        for e in options:
            z += e
        if int(z) not in primes: # might be faster if primes is generated all at once, rather than repeated testing
            return False
        results.append(z)
    return True
    
res = []
primes = [2]
for n in range(3,1000000,2):
    if isPrime(n):
        primes.append(n)
for e in primes:        
    if rotation(str(e)):
        res.append(e)
        
print len(res)