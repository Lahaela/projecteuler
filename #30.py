# make a loop to check all numbers
n = 1
answers = []
while int(len(str(n))) <= 7: # reasonable end point
    n += 1
    total = 0 # reset each test so keep in loop
    for digitpos in range(0, int(len(str(n)))): #clean up later switching between int and str
        total += int((str(n))[digitpos])**5
    if n == total:
        answers.append(n)

print sum(answers)

