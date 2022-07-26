def longesOnes(nums, k):
    maxLength = 0
    myDict = {0: 0, 1: 0}
    windowStart = 0
    for windowEnd in range(len(nums)):
        myDict[nums[windowEnd]] += 1
        if myDict[0] > k:
            myDict[nums[windowStart]] -= 1
            windowStart += 1
        else:
            length = (windowEnd - windowStart) + 1
            maxLength = max(length, maxLength)
    return maxLength

print(longesOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))