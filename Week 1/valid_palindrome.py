class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalString = (''.join(char for char in s if char.isalnum())).lower()
        first = 0
        last = len(normalString)-1
        for char in normalString:
            if (normalString[first] != normalString[last]):
                return False
            first += 1
            last -= 1

        return True
