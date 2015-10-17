x = 600851475143
y = 1
while y < x:
    if x % y == 0:
        x = x / y
        print y
        y = y + 1
    else:
        y = y + 1
print x, y