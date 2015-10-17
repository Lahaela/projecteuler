#Palindrome procedure -- check
def iter_palindrome(s):
    s = str(s)
    for i in range(0, len(s)/2):
        if s[i] != s[-(i+1)]:
            return False
    return True

res = []
for n in range(1,1000000):
    # base 10 first
    if iter_palindrome(n):
        b = str(bin(n))[2:]
        # if not palindromic, remove from res
        if iter_palindrome(b):
            res.append(n)

print res
print sum(res)