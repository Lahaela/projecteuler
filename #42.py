
alphabet_value = {'"':0,'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,
                'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}               

fhand = open('words.txt')

#generate
hold = fhand.read().split(',')
triangle = []
for n in range(1,25):
    triangle.append(n*(n+1)/2)
res = []
count = 0

value = []
for e in hold:
    z = 0
    for char in e:
        z += alphabet_value[char]
    value.append(z)

for p in value:
    if p in triangle:
        count += 1
        
print count