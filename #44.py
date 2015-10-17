# initialization
pentagonal = []
n = 1
res = []
tested = []

while n < 10: # reasonable number
    pentagonal.append(n*(3*n-1)/2)
    for e in pentagonal:
        for p in pentagonal:
            if [e,p] in tested:
                continue
            if (e+p) in pentagonal:
                if (e-p) or (p-e) in pentagonal:
                    print [e,p]
                    break
                else:
                    tested.append([e,p])
            else:
                tested.append([e,p])
    n += 1