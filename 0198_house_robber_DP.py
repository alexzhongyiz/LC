def rob(nums):
    
    dp = [0 for _ in range(len(nums))]
    dp[0] = nums[0]
    if len(nums)>1:
        dp[1] = max(nums[0],nums[1])
    
    for i in range(2,len(nums)):
        dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        print(i,dp[i])
    return dp[-1]

def rob_cir(nums):
    if len(nums)<=3:
        return max(nums)
    
    dp = [(0,0) for _ in range(len(nums))]
    dp[0] = (nums[0],0)
    dp[1] = (max(nums[0],nums[1]),nums[1])
    tmp = max(nums[0],nums[1])
    for i in range(2,len(nums)-1):

        include0 = max(dp[i-1][0],dp[i-2][0]+nums[i])
        noinclude = max(dp[i-1][1],dp[i-2][1]+nums[i])
        dp[i] = (include0,noinclude)
        print(i,dp[i])
        tmp = max(max(tmp,include0),noinclude)
    dp[len(nums)-1] = (0,max(dp[len(nums)-2][1],dp[len(nums)-3][1]+nums[-1]))
    print(dp[-1])
    return max(tmp, dp[-1][1])
    


#print(rob([3,1,5,7,4]), rob([1,2,3,1]),rob([2,7,9,3,1]))
print(rob_cir([4,1,2,7,5,3,1]))