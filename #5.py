x = 1
smallest = 0
while smallest != x:
    if x%11==0 and x%12==0 and x%13==0 and x%14==0 and x%15==0 and x%16==0 and x%17==0 and x%18==0 and x%19==0 and x%20==0:
        smallest = x
    else:
        x = x + 1
print smallest