# Roger
def isPrime(number):
    for x in range (2,number):
        if (number % x == 0):
            return False
    return True    

first = 2 
count = 0
while (count < 10001): 
    if (isPrime(first)):
        count += 1 # shorthand for count = count + 1
    first += 1 # count is only updated with primes, while first is constantly updated
print first
    
