# Given An Array Of N integers and a Number K return max sum of subarray of size k that has K Distinct Elements. if it does not exist return -1.

# Test Case:
# [1,2,3,4,4,3,2,1],k=3
# Output:
# 9
# [1,2,3],[2,3,4],[4,3,2],[3,2,1] are valid subarrays as they have k distinct elements.max sum among them is 9

# Test Case:
# [1,2,2] k=3
# Output:
# -1
# No valid subarray of length k exist that has all k elements unique.

# Constrainst:
# 1<=n<=1e5
# k<=n
# 1<=arr[i]<=1e9

def maxSumSizeKUnique(arr, k):
    numberSet = set()
    windowStart, maxSum = 0, 0
    currSum = 0

    for windowEnd in range(len(arr)):
        currSum += arr[windowEnd]
        while arr[windowEnd] in numberSet:
            numberSet.remove(arr[windowStart])
            currSum -= arr[windowStart]
            windowStart += 1
        numberSet.add(arr[windowEnd])
        if (windowEnd - windowStart) + 1 < k:
            continue
        elif (windowEnd - windowStart) + 1 == k:
            maxSum = max(maxSum, currSum)

    if maxSum == 0:
        return -1
    return maxSum

print(maxSumSizeKUnique([1,2,3,4,4,3,2,1],3)) # 9
print(maxSumSizeKUnique([1,2,2,1,3,4],4)) # 10
print(maxSumSizeKUnique([1,1],5)) # -1
print(maxSumSizeKUnique([1,2],2)) # 3
