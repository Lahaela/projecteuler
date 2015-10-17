sumsq = 0
x = 1
while x <= 100:
    sumsq = sumsq + (x*x)
    x = x + 1
print sumsq
 
total = 0
x = 1
while x <= 100:
    total = total + x
    x = x + 1
sqsum = total * total
print sqsum

diffsqsum = sqsum - sumsq
print diffsqsum