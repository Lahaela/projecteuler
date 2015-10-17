def isPrime(number): # inefficient, but clean--repetitively checks for prime
                    # perhaps more efficient to generate list of primes? -Vlad, Mr.E
    for x in range (2,number):
        if (number % x == 0):
            return False
    return True   
    
n = 7 # under 100, begin at 3 and add 2
        # under 1000, begin at 7
        # as number gets larger, successive primes more far apart means begins farther down list
total = 0
while total <= 1000000:
    if isPrime(n):
        total += n
        if isPrime(total) and total <= 1000000:
            # if begin at 3, change total to total+2 -Nate
            print total
    n += 2
