from collections import Counter
def minPackage(arr):
    freqMap = Counter(arr)
    res = 0
    for v in freqMap.values():
        if v > 2:
            res += v // 3
            v = v % 3
        if v > 1:
            res += v // 2
            v = v % 2
        if v == 1:
            return -1
    return res

print(minPackage([1,8,5,8,8,8,5,1,8]))