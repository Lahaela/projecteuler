import re

hand = open('stuff.txt') # based on the downloaded file
database = {}
count = 0
for line in hand:
    database[count]=line
    count +=1
    #database[count]=line #store the entire file for now

T = int(database[0])
v = re.compile(r'(^(.?+)(#+)(.+)$)|(^(.+)(#+)(.?+)$)')
answer = "NO"

for a in range(1,count+1):
    if (re.search('[0-9]', database[count])): #save number info
        N = int(database[count])
        for i in range(1,N+1):
        	m = re.match(v,database[count+i])
        	if m:
        		l = m.end()-m.start()
        		for y in range(1,l):
					