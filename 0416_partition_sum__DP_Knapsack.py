import functools
def canPartition( nums) -> bool:
    total = sum(nums)
    if total%2:
        return False
    half = total//2
    dp = [[False]*len(nums)]*(half+1)
    for i in range(len(nums)):
        dp[0][i] = True
        for j in range(half+1):
            dp[j][i] = dp[j][i-1] if j<nums[i] else (dp[j][i-1] or dp[j-nums[i]][i-1])
            print(i,j,dp[j][i])
    return dp[half][len(nums)-1]

    # @functools.lru_cache
    # def dp(i,sum):
        # if sum ==0:
        #     return True
        # if sum < 0 or i<0:
        #     return False
        # return dp(i-1,sum) or dp(i-1,sum-nums[i])
    
    #return dp(len(nums)-1,half)


print(canPartition([2,3,4,5]), canPartition([2,3,4]))
