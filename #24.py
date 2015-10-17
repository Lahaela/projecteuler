# predicted to take 3 hours based on timeclock
import random
def factorial(tralala):
    if tralala <= 1:
        return 1
    else:
        return tralala*factorial(tralala-1)

def rotation(lala):
    global options
    results = []
    while len(results) < factorial(len(options)):
        m = options[:]
        z = random.choice(m)
        m.remove(z)
        while len(z) < len(options):
            y = random.choice(m)
            m.remove(y)
            z += y
        if z not in results:
            results.append(z)
    results.sort()
    return results
    
options = ['0','1','2','3','4','5','6','7','8','9'] # must be strings for concatenation
res = rotation(options)
print len(res)
print res[1000000]
print res[999999]
# 720 --> 3628800