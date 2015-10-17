def isPrime(number):
    for x in range (2,number):
        if (number % x == 0):
            return False
    return True    

first = 3 
total = 0
while (first < 2000000): 
    if (isPrime(first)):
        total = total + first 
    first += 2
print total + 2
    