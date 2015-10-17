#n65.py
from fractions import Fraction

count = 99
x = Fraction(1,1) # IVP
while count>1:
	if count%3==0:
		x = x**-1 + count/3*2
	else:
		x = x**-1 + 1
	count -= 1

x= 2+x**-1
res = list(str(x))
j = 0
for i in range(0,res.index('/')):
	j += int(res[i])
print j

