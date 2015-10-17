res = []

for a in range(1,10001):
    divA = [1]
    for i in range(2,int(a**0.5+1)): #sqrt >> minimal loops
        if a%i==0 and (a/i not in divA):
            divA.append(i)
            if i!=a/i: #avoid repeat of sqrt
                divA.append(a/i)
    for b in range(1,10001):
        if b >= a:
            divB = [1]
            for j in range(2,int(b**0.5+1)):
                if b%j==0 and (b/j not in divB):
                    divB.append(j)
                    if j!=b/j:
                        divB.append(b/j)
        if sum(divA)==b and sum(divB)==a and a!=b:
            res.append([a,b])
            break
    
print res

total = 0
for e in res:
    total += e[0] + e[1]
print total