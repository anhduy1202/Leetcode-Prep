class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left <= right:
            middle = left+(right-left)//2
            if nums[middle] == target:
                return middle
            elif target > nums[middle]:
                left += 1
            elif target < nums[middle]:
                right -= 1
        return -1
