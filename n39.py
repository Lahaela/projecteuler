## 39
import math

def isLegal(a, b, c):
    if a > b + c or b > a + c or c > a + b:
        return False
    return True

data = {}
for a in range(1, 1000):
    for b in range(1, 1000):
        c = math.sqrt(a**2 + b**2)
        d = int(c)
        if c == d and isLegal(a, b, c):
            tmp = data.get(a+b+d, [])
            tmp.append((a, b, d))
            data[a+b+d] = tmp


m = 0
p = 0
for k in data:
    if k <= 1000 and len(data[k]) > m:
        m = len(data[k])
        p = k

print("p:", p, "m:", m)
# There are duplicates because I don't enforce b > a
# I don't enforce it because of the case where b == a
# m is exactly double the true number of solutions
# Solution is p = 840, m = 16 --> 8
