def longestRepeat(s, k):
    hashMap = {}
    maxLength = 0
    left, right = 0, 0
    counter = 0
    while right < len(s):
        hashMap[s[right]] = hashMap.get(s[right], 0)+1
        if ((right - left) + 1) - max(hashMap.values()) <= k:
            counter += 1
            maxLength = max(maxLength, counter)
            right += 1
        else:
            hashMap[s[left]] = hashMap.get(s[left], 0)-1
            left += 1
            right += 1

    return maxLength


print(longestRepeat("AABABBA", 1))
