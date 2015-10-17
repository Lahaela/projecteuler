#functions
def factorial(n):
    x = n
    while n > 1:
        n -= 1
        x *= n
    return x
        
def combination(y, z):
    return factorial(y)/factorial(z)/factorial(y-z)

count = 0    
for top in range(1,101):
    for bottom in range(1, 101):
        if (bottom<top) and (combination(top, bottom) > 1000000):
            count += 1
print count

#4075