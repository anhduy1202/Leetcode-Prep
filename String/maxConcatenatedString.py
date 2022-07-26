from collections import Counter


class Solution:
    def __init__(self, arr) -> None:
        self.arr = arr

    def maxLength(self, arr):
        mySet = set()
        def overlap(mySet,s):
            c = Counter(mySet) + Counter(s)
            return max(c.values()) > 1
        
        def backtrack(i):
            if i == len(arr):
                return len(mySet)
            res = 0
            if not overlap(mySet,arr[i]):
                for c in arr[i]:
                    mySet.add(c)
                res = backtrack(i+1)
                for c in arr[i]:
                    mySet.remove(c)
            return max(res,backtrack(i+1))
        
        return backtrack(0)


sol = Solution(["aa", "bb"])
print(sol.maxLength(["cacc", "b"]))
print(sol.maxLength(["un", "iq", "ue"]))
print(sol.maxLength(["cha", "r", "act", "ers"]))
