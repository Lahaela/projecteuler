primes = [2] #perhaps generating list is faster
            # this still took, seriously, 11+ hours. Ridiculosu.
n = 3

while n < 2000000:
    test = True # must reset after each non-Prime
    for x in range (3,n**0.5,2):
        if (n % x == 0): # must loop after each failed test until all options are failed
            test = False # still very inefficient
            break
    if test:
        primes.append(n)
        print primes[-1]
    n += 2
            
print sum(primes) # sums after list is generated