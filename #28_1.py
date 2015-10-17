simplyadd = 8
diagtotal,count,simply = 1,1,1

for n in range(1,1001,2): # to be a square, it has to be oddxodd
    simply += simplyadd
    diagtotal += simply*4 -count*12
    simplyadd += 8
    count += 1
    
print diagtotal