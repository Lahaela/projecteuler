#!/usr/bin/python

def repeatNum(s):
    d = list(str(s))
    if len(d)<10: d.insert(0,'0')
    for i in range(0,10):
        if d.count(str(i))!=1: return False
    return True
    
res = []
n = 123456789
count = 0
while n<9999999999:
    if repeatNum(n):
    	count += 1
    	if count == 1000000: 
    		print n
    		break
    n+=1