#n17

alphabet = {0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4}
abtens = {0:0,1:3,2:6,3:6,4:5,5:5,6:5,7:7,8:6,9:6}
abtweens = {11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8} #eleven ~ nineteen
total = 36 #initialize with 1~9


for x in range(10,1000):
	count = 0
	if x%100!=x: 
		count+=10 #10 = len('hundredand')
		if x%100==0: count-=3
		count += alphabet[int(str(x)[-3])]
	if x%100 in abtweens: count+=abtweens[x%100]
	else:
		count += abtens[int(str(x)[-2])] + alphabet[int(str(x)[-1])]
	total += count

total += 11 #len('onethousand')
print total

# one ten +0
# two twenty +3
# three thirty +1
# four fourty +2
# five fifty +1
# six sixty +2
# seven seventy +2
# eight eighty +1
# nine ninety +2
