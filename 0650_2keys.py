import math
def minsteps(n):
    # following using greedy, wrong, eg. return 6 when n =5, should have done is copy 1 and paste 4 times.
    if n==1:
        return 0
    currT = 1
    res = 0
    while currT < n and 2*currT <= n:
        currT *= 2
        res += 2
    if n==currT:
        return res
    else:
        last_copy = currT//2
        if n == currT+last_copy:
            res += 1
        else:
            res += 2

    return res


print(minsteps(1), minsteps(2),minsteps(3),minsteps(4))