total = 0
for x in range (1,1000):
    if x % 3 == 0 or x % 5 == 0:
        total = total + x
print 'Total: ', total 

#Take every # between 1 and 1000
#Test to see if multiple of 3
#Test to see if multiple of 5
#If test is successful
#Add the number to the 'total'
# at the end of the 1000, 'total' represents the sum of all these numbers

total = 0
x = 1
while x < 1000:
    if x % 3 == 0 or x % 5 == 0:
        total = total + x
    x = x + 1
print 'Total: ', total 