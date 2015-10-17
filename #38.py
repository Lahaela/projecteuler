def repeatEl(s):
    d = list(str(s))
    for i in d:
        if '0' in d: return False
        if d.count(i)>1: return False
    return True
    
def panCheck(f1):
    d2 = list(f1)
    if len(d2)!=9: return False
    d2 = map(int,d2)
    if d2.count(0)!=0 : return False
    for i2 in range(1,10):
        if d2.count(i2)!=1 : return False
    return True

seq = [1, 2, 3, 4, 5, 6, 7]
    
input = [n for n in range(2,9876) if repeatEl(n)]
ans = 0
for a in input:
    z = str(a)
    g = 1
    while len(z)<9:
        z+=str(a*seq[g])
        g+=1
    if panCheck(z) and int(z)>ans: ans=int(z)
    print ans
