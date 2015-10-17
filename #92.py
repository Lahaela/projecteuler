def digiNext(n):
    next = 0
    for digitpos in range(0, int(len(str(n)))): #taken from 30.py
        next += int((str(n))[digitpos])**2
    return next

i = 0
count = 0
while i < 10000000: # not equal to because 10000001 adds to count
    i += 1
    temp = i # struggled w/ using i w/o changing value --> alias
    z = 'notdone'
    while (z != 'done'):
        temp = digiNext(temp)
        if temp == 89:
            count += 1
            z = 'done' # attempt using break later
        if temp == 1:
            z = 'done'
print count
        
    