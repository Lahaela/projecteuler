def gimmePrimes(upperRange):

    #stuff
    primes = []
    unPrimality = False
    
    #loop through odd value until upper range
    for i in range(3, upperRange, 2):
    
        if(i%101 == 0): print i #debug stuff
        
        #loop through primes lower than i/2
        for prime in primes[0:int(i/2)]:
            if(i % prime == 0):
                unPrimality = True
                break
        if(unPrimality):
            unPrimality = False
            continue
        else:
            primes.append(i)
            unPrimality = False

    return [2] + primes

print gimmePrimes(1000000)