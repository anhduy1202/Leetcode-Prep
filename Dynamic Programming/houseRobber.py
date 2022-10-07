def houseRobbermemo(nums):
    memo = {}
    def dp(i):
        if i == 0:
            return nums[0]
        if i == 1:
            return max(nums[0], nums[1])
        if i not in memo:
            memo[i] = max(dp(i-1), nums[i] + dp(i-2))
        return memo[i]
    
    return dp(len(nums)-1)
                

def houseRobber(nums):
    rob1,rob2 = 0,0
    for num in nums:
        temp = max(rob1+num,rob2)
        rob1 = rob2
        rob2 = temp
    return rob2

print(houseRobbermemo([2,1,1,2]))