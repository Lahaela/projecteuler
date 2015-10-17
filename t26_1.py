def prime(x):
	for n in range(2,int(x**0.5)):
		if x%n==0:
			return False
	return True

def cycle(d):
	#return len(str((10**(d-1))/d))
	d1 = str((10**(d-1))/d)
	print '*', d1
	for y in range(1,(len(d1)/2)+1):
		if d1[:y]==d1[y:2*y]:
			print 'bye'
			return len(d1[:y])
	return len(d1)


#res = {}
ma = 1
#for i in range(17,1000): # cut out the first 16 because I know it's not in there
#	if prime(i):
#		if cycle(i)>ma: 
#			ma=cycle(i)
#			print i
#		res[i]= cycle(i)
print cycle(983)
print cycle(991)
#print ma
#print max(res, key=res.get)