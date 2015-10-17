def repeatNum(s):
    d = list(str(s))
    for i in d:
        if '0' in d: return False
        if d.count(i)>1: return False
    return True
    
def countR(f1, f2, f3):
    d2 = list(str(f1)+str(f2)+str(f3))
    if len(d2)!=9: return False
    d2 = map(int,d2)
    if d2.count(0)!=0 : return False
    for i2 in range(1,10):
        if d2.count(i2)!=1 : return False
    return True

pancakes1 = []  
n = 2 # doesn't change if 1 bxc repeat bad
while n<=987: #987654321 length of 3
    if repeatNum(n): pancakes1.append(n)
    n+=1
pancakes2 = pancakes1[:]
while n<=9876: #987654321 length of 4
    if repeatNum(n): pancakes2.append(n)
    n+=1

res = []        
res = [a*b for a in pancakes1 for b in pancakes2 if (b>a and (countR(a,b,a*b)))]
for el in res:
    if res.count(el)>1 : res.remove(el)
print 'Sum: ', sum(res)