## 57

class fraction:
    def __init__(self, numerator, denominator):
        self.numer = numerator
        self.denom = denominator

    def reciprocal(self):
        self.numer, self.denom = self.denom, self.numer

    def addOne(self):
        self.numer += self.denom

count = 0
x = fraction(3, 2)
for _ in range(1001):
    x.addOne()
    x.reciprocal()
    x.addOne()
    if len(str(x.numer)) > len(str(x.denom)):
        count += 1

print(count)