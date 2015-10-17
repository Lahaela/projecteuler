# generate
pentagonal = []
n = 1
for n in range(1000,10000):
    pentagonal.append(n*(3*n-1)/2)
    n += 1

z = False # to avoid double printing
for e in pentagonal:
    for p in pentagonal:
        if (p>e) and ((e+p) in pentagonal) and ((p-e) in pentagonal):
            print [e,p]
            print p-e
            z = True
            break
    if z:
        break
        