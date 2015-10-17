numbers = [] # generate list first
repeat = [] # if many repeats, put in list

# now get the list, in order
for a in range(2,101):
    for b in range (2,101):
        x = a**b
        numbers.append(x)
numbers.sort()

# find repeats
for number in range(0,int(len(numbers))-1): #subtract 1 because next line adds 1, avoid going out of index
    if numbers[number] == numbers[number+1]:
        repeat.append(number)
    number += 1

# delete repeats
for pos in repeat:
    del numbers[pos]

print len(numbers)