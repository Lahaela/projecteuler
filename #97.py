# we multiply from right to left, so splicing to last 15 digits preserves value
#avoids overflow

#initialize
count = 1
res = 2

while count < 7830457: #Mersenne condition
    res = res*2
    if len(str(res)) > 15:
        res = int(str(res)[-15:])
    count += 1
    
print str(res*28433+1)[-10:]