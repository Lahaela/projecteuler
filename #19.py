#list with days in month order
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
calendar = {'January':31, 'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31, 'November':30, 'December':31}

date = 1
count = 0
year = 1900
while year<2000:
    if year%4==0 and year!=1900: calendar['February']=29
    else: calendar['February']=28
    for month in months:
        date += calendar[month]
        if date%7==0: count+=1
    year+=1
    
print count
#answer is 171, one less than result?