x = 1
count = 0
while x <= 50:
    x += 1
    for n in range(1,50):
        if n == int(len(str(x**n))):
            count += 1
print count + 1 # 1**1 is NOT counted