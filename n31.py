#Problem 31

def count_change(amount):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    def helper(amount, coinsidx):
        if coinsidx >= len(coins):
        	return 0
        if amount<=0:
            return 1
        if coins[coinsidx] > amount:
            return 0

        return helper(amount-coins[coinsidx], coinsidx) + helper(amount, coinsidx+1)
    return helper(amount,0)

a = count_change(200)
print(a)