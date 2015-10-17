first = 3
total = 0
z = True
while first < 2000000:
    for x in range (2,first):
        if (first % x == 0):
            z = False
            break
    if (z):
        total += first
    first += 2
print total + 2