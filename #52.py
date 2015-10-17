#initialize
n = 1
def sameDigi(a):
    temp = []
    for s in str(a):
        temp.append(s)
    temp.sort()
    if temp != digi:
        return False
    return True

while True:
    digi = [] #restart per number
    for i in str(n):
        digi.append(i)
    digi.sort()
    if sameDigi(2*n):
        if sameDigi(3*n):
            if sameDigi(4*n):
                if sameDigi(5*n):
                    if sameDigi(6*n):
                        print n
                        break
    n += 1     