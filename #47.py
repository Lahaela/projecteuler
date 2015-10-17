def isPrime(number):
    for x in range (2,int(number**0.5+1)):
        if (number % x == 0):
            return False
    return True
    
generate = []
gen = 2
while len(generate)<250: #raised from 100 for 4
    if isPrime(gen):
        generate.append(gen)
    gen+=1
    
def factors(n):
    div = [1]
    for x in range(2,int(n**0.5)+1):
        if n%x==0:
            div.append(x)
            if x != n/x:
                div.append(n/x)
    return div

res = []
resii = []
m = 2
while True:
    for s in factors(m):
        if s in generate:
            res.append(s)
    if len(res)==4: #change
        resii.append(m)
    res = []
    m +=1
    for a,b in enumerate(resii[:-3]):
        if resii[a+1]==(b+1) and resii[a+2]==(b+2) and resii[a+3]==(b+3):
            print b, b+1, b+2, b+3
            quit()
            
# worked for 2 and 3
# not 238203