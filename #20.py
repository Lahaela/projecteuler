def digit_addition(n):
    pos = 0
    total = 0
    n = str(n)
    while pos < len(n):
        digit = int(n[pos])
        total += digit
        pos += 1
    return total
    
n = 100
product = 1
while n > 0:
    product = product * n
    n += -1
    
print digit_addition(product)