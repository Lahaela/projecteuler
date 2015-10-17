# from __future__ import division
from itertools import permutations

def sieve(n):
	lst = range(n+1)
	lst[1] = 0
	sqrtn = int(round(n**0.5))
	for i in range(2, sqrtn+1):
		if lst[i]:
			lst[i*i:n+1:i] = [0] * len(range(i*i,n+1,i))
	return filter(None,lst)

def permute(n):
	perms = [''.join(p) for p in permutations(str(n))]
	perms = [int(el)-n for el in perms if int(el) in primes]
	return set(perms)

primes = filter(lambda x: x>1000 and x<10000,sieve(10000))
for i in primes:
	options = permute(i)
	for diffs in options:
		if diffs!=0 and 2*diffs in options:
			print(i, options)
			break