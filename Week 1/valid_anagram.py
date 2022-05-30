class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = dict()
        for char in s:
            hashMap[char] = hashMap.get(char, 0)+1
        for char in t:
            hashMap[char] = hashMap.get(char, 0)-1
        for v in hashMap:
            if hashMap[v] != 0:
                return False
        return True
