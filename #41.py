def isPrime(number):
    for x in range (2,int(number**0.5+1)):
        if (number % x == 0):
            return False
    return True    
    
def repeatNum(s):
    d = list(str(s))
    for i in d:
        if d.count(i)>1:
            return False
    return True
    
def countdown(m, f):
    t = 9
    while t>m:
        if str(t) in str(f):
            return False
        t -= 1
    return True
    
res = []
for n in range(7123456, 7777777):
    if countdown(7, n) and repeatNum(n) and isPrime(n):
        res.append(n)
        
print res
print max(res)