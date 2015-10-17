#Palindrome procedure -- check
def iter_palindrome(s):
    s = str(s)
    for i in range(0, len(s)/2):
        if s[i] != s[-(i+1)]:
            return False
    return True

# generate base10
res = []
for n in range(2,100): #1 doesn't count
    if iter_palindrome(n):
        res.append(n)

print res
# convert to binary -- bin function
verify = []
binary = []
for e in res:
    b = str(bin(e))[2:]
    binary.append(b)
    # if not palindromic, remove from res
    if not iter_palindrome(b):
        res.remove(e)
    if iter_palindrome(b):
        verify.append(e)

print res
print verify
print binary