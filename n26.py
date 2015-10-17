import re
# if the denominator's prime factorization contains non-2 or non-5, it is repeating
def repeating(n):
	i = 2
	while i!=n:
		if n%i==0:
			factors=[]
			if i not in factors: factors.append(i)
			n/=i
		else:
			i+=1
	factors.append(i)
	for f in factors:
		if f!=2 and f!=5:
			return True
	return False

def isPrime(x):
	i = 2
	while i<x:
		if x%i==0: return False
		else: i+=1
	return True


