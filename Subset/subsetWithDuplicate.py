def subsetWithDupe(nums):
    list.sort(nums)
    subsets = [[]]
    startIdx,endIdx = 0,0
    for i in range(len(nums)):
        startIdx = 0
        if i > 0 and nums[i-1] == nums[i]:
            startIdx = endIdx + 1
        endIdx = len(subsets) - 1
        for j in range(startIdx,endIdx+1):
            set1 = list(subsets[j])
            set1.append(nums[i])
            subsets.append(set1)
    return subsets

print(subsetWithDupe([1,2,2]))