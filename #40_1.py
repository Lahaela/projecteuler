# initialization
fraction = []
n = 1

while len(fraction) < 1000001:
    for m in range(0,len(str(n))):
        fraction.append(str(n)[m])
        fraction[-1] = int(fraction[-1])
    n += 1
    
# the nth digit is -1 because positions start at 0
print fraction[0]*fraction[9]*fraction[99]*fraction[999]*fraction[9999]*fraction[99999]*fraction[999999]