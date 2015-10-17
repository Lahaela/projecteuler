#n89.py

def popper(s,sub,v,y): #v = value of letter, y = value of line s
	if sub not in s: return y, s
	else:
		y += v
		s = s[:s.find(sub)]+s[s.find(sub)+len(sub):]
		return popper(s,sub,v,y)

def decon(s1,sub1,v1,y1):
	if y1<v1:
		return y1, s1
	else:
		y1 -= v1
		s1 += sub1
		return decon(s1,sub1,v1,y1)


hand = open('tests.txt') #input file name
# finding the value
for line in hand:
	val = 0
	init=len(line)
	init1=line
	val, line = popper(line[:-1],'CM',900,val) #remove newline
	val, line = popper(line,'CD',400,val)
	val, line = popper(line,'XC',90,val)
	val, line = popper(line,'XL',40,val)
	val, line = popper(line,'IX',9,val)
	val, line = popper(line,'IV',4,val)
	val += line.count('M')*1000+line.count('D')*500+line.count('C')*100+line.count('L')*50+line.count('X')*10+line.count('V')*5+line.count('I')
	print val
	linef = '' #below order is bad because of 1800, 2800, etc.
	val, linef = decon(linef,'M',1000,val)
	val, linef = decon(linef,'CM',900,val)
	val, linef = decon(linef,'D',500,val)
	val, linef = decon(linef,'CD',400,val)
	val, linef = decon(linef,'C',100,val)
	val, linef = decon(linef,'XC',90,val)
	val, linef = decon(linef,'L',50,val)
	val, linef = decon(linef,'XL',40,val)
	val, linef = decon(linef,'X',10,val)
	val, linef = decon(linef,'IX',9,val)
	val, linef = decon(linef,'V',5,val)
	val, linef = decon(linef,'IV',4,val)
	val, linef = decon(linef,'I',1,val)
	print init-len(linef)-1, '|', linef
	print init1, '|', linef