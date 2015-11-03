# 76

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def helper(amount, coinsize):
        if amount<=0:
            return 1
        if coinsize > amount:
            return 0
        # print(amount, coinsize)

        return helper(amount-coinsize, coinsize) + helper(amount, coinsize+1)
    return helper(amount,1)

print(count_change(100))

#190569291