def isPythagorean(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False
        
for a in range(1,1000):
    for b in range(1,1000):
        for c in range(1,int((a**2+b**2)**0.5+1)):
            if a+b+c==1000 and(isPythagorean(a,b,c)):
                print a*b*c
                exit()
                