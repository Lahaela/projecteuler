#Fibonacci sequence
total = 0
x = 1
y = 2
while y < 10 and x < 10:
    x = x + y
    y = x + y
    total = total + x + y
print 'Total: ', total - y + 3 