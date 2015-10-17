def special(s,di2, val):
	for i in range(0,len(s)):
		if s[i:i+2] in di2:
			val += di2[s[i:i+2]]
			s = s[:i] + s[i+2:]
			try: s, val = special(s, di2,val)
			except: return s,val
	return s, val

def parse (s, di, di2):
	s, val = special(s,di2,0)
	for i in s:
		val += di[i]
	return val

def identify(n2, di):
	possib = [1]
	for z in di:
		if z<=n2: possib.append(z)
	return max(possib)

def out(n1, di):
	s = ""
	while n1!=0:
		ide = identify(n1,di)
		s = s + di[ide]
		n1 -= ide
	return s

#clusterfuck of dict creation
romabet = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
inv_romabet = {v:k for k, v in romabet.items()} # dict comprehension!
inv_romabet2 = {4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
romabet2 = {v:k for k, v in inv_romabet2.items()}
inv_romabet.update(inv_romabet2)

hand = open("roman.txt")
ans = 0
for line in hand:
	y = parse(line[:-1],romabet,romabet2) #-1 strips \n
	new = out(y,inv_romabet)
	res = len(line)-len(new)-1
	ans += res

print ans