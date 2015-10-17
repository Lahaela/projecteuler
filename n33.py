def reducedFraction(x,y):
	if float(str(x)[0])/float(str(y)[1]) == x/float(y): return (x,y)
	return False

def nontrivial(i,j):
	if str(i)[-1]=='0' and str(j)[-1]=='0': return False
	return True

res = []
for a in range(10,100):
	for b in range(10,100):
		if b>a and str(b)[-1]!='0' and str(a)[1]==str(b)[0] and nontrivial(a,b) and reducedFraction(a,b): res.append(reducedFraction(a,b))

print res