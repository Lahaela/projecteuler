
alphabet_value = {'"':0,'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,
                'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
                
fhand = open('names.txt')

#generate
hold = fhand.read().split(',')
hold.sort()

value = []
for e in hold:
    z = 0
    for char in e:
        z += alphabet_value[char]
    value.append(z)

res = []
count = 0
for n in value:
    count += 1
    res.append(count*n)
    
print sum(res)