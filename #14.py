largest = 1
for n in range(1,1000000): 
    count = 1 #initialize
    z = n #alias
    while n != 1:
        if n%2==0:
            n = n/2
        else:
            n = 3*n+1
        count += 1
    if count > largest:
        largest = count
        m = z
        
print [m,largest]