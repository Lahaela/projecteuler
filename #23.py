def divisors(n):
    div = [1]
    for x in range(2,int(n**0.5)+1):
        if n%x==0:
            div.append(x)
            if x != n/x:
                div.append(n/x)
    return sum(div)

abundance = []
deficience = []
for m in range(1, 28124):
    if divisors(m)>m:
        abundance.append(m)
    deficience.append(m)

for a in abundance:
    for b in abundance:
        if b>=a and (a+b in deficience):
            deficience.remove(a+b)
            
print 'answer:', sum(deficience)

