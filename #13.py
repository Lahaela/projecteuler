fhand = open('#13file.txt')
sum = 0
for line in fhand:
    line = int(line)
    sum += line
sum = str(sum)
print sum[:10]