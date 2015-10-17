def iter_palindrome(s):
    s = str(s)
    for i in range(0, len(s)/2):
        if s[i] != s[-(i+1)]:
            return False
    return True  
    
def reverse(r):
    r = str(r)
    return int(r[::-1])
    
lychrel = 0
for n in range(10,10000):
    n+=reverse(n) # takes palindromes that are Lychrel numbers into account
    count = 1
    while not iter_palindrome(n) and count<50:
        n+=reverse(n)
        count +=1
    if not iter_palindrome(n) and count>=50:
        lychrel +=1
        
print lychrel