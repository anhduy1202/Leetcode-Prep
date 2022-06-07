class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            if i > 0 and numbers[i-1] == numbers[i]:
                continue
            l,r = 0, len(numbers)-1
            while l < r:
                twoSum = numbers[l] + numbers[r]
                if twoSum > target:
                    r -= 1
                elif twoSum < target:
                    l += 1
                else:
                    return [l+1,r+1]