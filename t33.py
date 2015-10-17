
#test cases
def reducedFraction(x,y):
	print float(x)/float(y)
	print int(str(x)[:1])/float(str(y)[-1])
	if int(str(x)[:1])/float(str(y)[-1]) == x/float(y): return (x,y)
	return False

#print reducedFraction(30,50)
print reducedFraction(11,22)