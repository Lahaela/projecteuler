# initialization
n = 1
triangle = []
pentagonal = []
hexagonal = []
z = False

for n in range(10000,100000):
    triangle.append(n*(n+1)/2)
    pentagonal.append(n*(3*n-1)/2)
    hexagonal.append(n*(2*n-1))
    
for e in triangle:
    if e in pentagonal:
        if e in hexagonal:
            print e
            z = True
            break
        if z:
            break
    if z:
        break
        