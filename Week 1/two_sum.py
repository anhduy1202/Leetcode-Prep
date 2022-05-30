class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        for idx, val in enumerate(nums):
            diff = target - val
            if diff not in hash_map:
                hash_map[val] = idx
            elif diff in hash_map:
                return [hash_map[diff], idx]
