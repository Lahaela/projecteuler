import math
index = 0
i = 0
res=[]
while index<=10**6: #change for tests
	i += 1
	r = list(str(i))
	for s in r:
		index += 1
		if int(math.log10(index))==(math.log10(index)):
			res.append(s)
answer = 1
print res
for x in res:
	answer *= int(x)
print answer