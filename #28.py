# initialize
upperrightadd = 8
upperleftadd = 6
lowerleftadd = 4
lowerrightadd = 2
diagtotal = 1
upperright = 1
upperleft = 1
lowerleft = 1
lowerright = 1

for n in range(1,1001,2): # to be a square, it has to be oddxodd
    upperright += upperrightadd
    upperleft += upperleftadd
    lowerleft += lowerleftadd
    lowerright += lowerrightadd
    diagtotal += upperright + upperleft + lowerleft + lowerright
    upperrightadd += 8
    upperleftadd += 8
    lowerleftadd += 8
    lowerrightadd += 8
    
print diagtotal