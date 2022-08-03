def nextGreater(nums1, nums2):
    stack = []
    hashMap = {i: -1 for i in nums2}

    for i in range(len(nums2)):
        while stack and nums2[stack[-1]] < nums2[i]:
            top = stack.pop()
            hashMap[nums2[top]] = nums2[i]
        stack.append(i)

    for i, num in enumerate(nums1):
        nums1[i] = hashMap[num]

    return nums1


print(nextGreater([4,1,2],[1,3,4,2]))
