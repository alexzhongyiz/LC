# Here used dfs with memorization for knapsack problem instead of lru cache as in 638 shopping offers.
# import functools
def findTargetSumWays(nums,target):
    # @functools.lru_cache()
    mem = {}
    def dfs(remains,tar):
        # remains = list(remains)
        if (remains,tar) in mem:
            return mem[(remains,tar)]
        if not remains:
            if tar !=0:
                return float('-inf')
            else:
                return 1
        else:
            tmp1 = dfs(tuple(remains[1:]),tar-remains[0]) if dfs(tuple(remains[1:]),tar-remains[0])>=0 else 0
            tmp2 = dfs(tuple(remains[1:]),tar+remains[0]) if dfs(tuple(remains[1:]),tar+remains[0])>=0 else 0
            mem[(tuple(remains),tar)] = tmp1+tmp2
            return tmp1+tmp2
    return dfs(tuple(nums),target)

print(findTargetSumWays([1,1,1,1,1],3))