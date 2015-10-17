#n46

def prime(i):
	if i%2==0: return False
	for j in range(3,int(i**0.5)+1,2):
		if i%j==0: return False
	return True

def goldbach(m):
	global primes
	for n in primes:
		if (((m-n)/2)**0.5).is_integer():
			return False
	return True

x = 3
primes = []
#composites = []
while True:
	if prime(x):
		primes.append(x)
	else:
		if goldbach(x):
			print x
			break
	x+=2
#		composites.append(x)
