x = 0
y = 1
count = 1
while True:
    x = x + y
    y = x + y
    count += 2
    x = str(x)
    y = str(y)
    if len(x)==1000:
        count = count - 1
        print count
        exit()
    elif len(y)==1000:
        print count
        exit()
    else:
        x = int(x)
        y = int(y)
