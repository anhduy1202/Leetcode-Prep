def contiguousArr(nums):
    hashMap = {}
    hashMap[0] = -1
    maxLength = 0
    count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        elif nums[i] == 1:
            count += 1

        if count in hashMap:
            maxLength = max(maxLength, i - hashMap[count])
        else:
            hashMap[count] = i
    return maxLength


print(contiguousArr([0, 0, 1, 0, 0, 0, 1, 1]))
