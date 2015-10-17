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
    
def rotation(lala):
    options = []
    count = []
    for char in range(0,len(lala)):
        options.append(lala[char])
    for p in options: # to keep z not in results below
        if p not in count:
            count.append(p)
    results = []
    while len(results) < factorial(len(count)):
        z = random.choice(options)
        for y in range(0, len(options)):
            if options[y] not in z:
                z += options[y]
        if not isPrime(int(z)):
            return False
        if z not in results:
            results.append(z)
    return True
    
res = [2]
n = 3
while n < 1000000:
    if isPrime(n):
        if rotation(str(n)):
            res.append(n)
    n += 2           
print len(res)