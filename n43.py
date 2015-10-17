## 43

pandigitals = []

def generate(string, left):
    if not left:
        pandigitals.append(string)
        return
    for x in left:
        newstring = string + str(x)
        newleft = left.copy()
        newleft.remove(x)
        generate(newstring, newleft)

left = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
generate("", left)
primes = [2, 3, 5, 7, 11, 13, 17]
for i in range(7):
    pandigitals = filter(lambda x: int(x[1+i:4+i]) % primes[i] == 0, pandigitals)
pandigitals = [int(x) for x in pandigitals]
print("Result:", sum(pandigitals))
