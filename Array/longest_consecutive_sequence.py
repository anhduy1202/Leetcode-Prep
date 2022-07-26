def longestSequence(nums):
    setNum = set(nums)
    res = 0
    for num in nums:
        if num - 1 not in setNum:
            larger = num + 1
            while larger in setNum:
                larger += 1
            res = max(res, larger-num)
    return res


print(longestSequence([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
