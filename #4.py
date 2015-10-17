#Palindrome procedure -- check
def iter_palindrome(s):
    s = str(s)
    for i in range(0, len(s)/2):
        if s[i] != s[-(i+1)]:
            return False
    return True
    
res = [] #initialization

for a in range(100,1000): #3 digit
    for b in range(100,1000):
        if iter_palindrome(a*b):
            res.append(a*b)
print max(res)