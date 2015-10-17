n = str(2**1000)
pos = 0
total = 0
while pos < len(n):
    digit = int(n[pos])
    total += digit
    pos += 1
print total