total = 0
n = 1
while n <= 1000:
    value = n**n
    n += 1
    total += value
        
total = str(total)
result = total[-10:]
print result