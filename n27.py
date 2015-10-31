# 27

def sieve(n):
    lst = range(n+1)
    lst[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn+1):
        if lst[i]:
            lst[i*i:n+1:i] = [0] * len(range(i*i,n+1,i))
    return filter(None,lst)

primes = sieve(100000)
bvals = sieve(1000)

currmax = 0
currval = (0, 0) # (a, b)
for b in bvals:
    avals = [x for x in range(-998, 1000) if 1+x+b in primes]
    for a in avals:
        n = 2
        while ((n+a)*n + b) in primes:
            n += 1
        if n > currmax:
            currmax = n
            currval = (a, b)

print(currval, currmax)
print currval[0]*currval[1]
# solution: (-61, 971) --> 71 primes
# product: -59,231