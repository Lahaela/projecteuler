def isPrime(number):
    for x in range (2,int(number**0.5+1)):
        if (number % x == 0):
            return False
    return True

def truncation(lala):
    lala = str(lala)
    results = []
    for n in range(0, len(lala)):
        results.append(lala[:n])
        if lala[n:] not in results:
            results.append(lala[n:])
    return results

res = []
z = 13 # 2, 3, 5, 7 don't count    
while len(res) < 11:
    flag = True
    for x in range (2,int(z**0.5+1)):
        if (z % x == 0):
            flag = False
            break
    if flag == True:
        options = truncation(z)
        verify = True
        for e in options:
            if e == '':
                continue
            if not isPrime(int(e)) or e=='1':
                verify = False
                break
        if verify == True:
            res.append(z)
    z += 2
      
print len(res)
print res
print sum(res)