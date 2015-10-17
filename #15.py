def plusFactorial(x):
    y = x
    while x>1:
        x -=1
        y += x
    return y

def countdown(p): 
    a = 0
    while p>1:
        a += hold[p]
        p-=1
    return a+1
 
hold = [0]
for m in range(1,21):
    hold.append(plusFactorial(m))

def answer(n):
    z = 1+n+hold[n]
    z += countdown(n)
    for q in range(1,n+1):
        z += countdown(q)
    return z
    
