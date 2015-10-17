x = 1
y = 1
numbers = [1]

while True:
    y = y + x
    numbers.append(y)
    z = sum(numbers)
    divisors = -1
    for a in range(1,int(z**0.5)): # much more efficient!
        if (z%a==0):
            divisors += 2
    if (divisors >= 500):
        print divisors, z
        break 