res = []

for a in range(3,1001):
    hold = []
    for n in range(1,2000): #kept on testing cap until reached same number twice
        rem = (((a-1)**n)+((a+1)**n))%(a**2)
        hold.append(rem)
    res.append(max(hold))
    
print sum(res)

# to make it faster, test for repeating sequences in hold and stop appending after a few iterations