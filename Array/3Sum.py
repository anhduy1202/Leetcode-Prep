def threeSum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i-1] == nums[i]:
            continue
        left, right = i + 1, len(nums)-1
        while left < right:
            threeSum = nums[i] + nums[left] + nums[right]
            if threeSum < 0:
                left += 1
            elif threeSum > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left-1] and left < right:
                    left += 1
    return res

print(threeSum([-1,0,1,2,-1,-4]))