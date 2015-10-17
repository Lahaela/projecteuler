def digiNext(n):
    next = 0
    for digitpos in range(0, int(len(str(n)))): #taken from 30.py
        next += int((str(n))[digitpos])
    return next

largest = 0
for a in range(1, 100):
    for b in range(1, 100):
        test = a**b
        result = digiNext(test)
        if result >= largest:
            largest = result
print largest