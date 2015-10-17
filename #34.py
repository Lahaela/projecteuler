def sumDigi(n):
    factorial = 1
    total = 0
    n = str(n)
    for digitpos in range(0,len(n)):
        digit = int(n[digitpos])
        while digit > 0:
            factorial = factorial * digit
            digit += -1
        total += factorial
        factorial = 1
    return total
        
x = 3
sum = 0
while len(str(x)) <= 5:
    x += 1
    if sumDigi(x) == x:
        sum += x
print sum