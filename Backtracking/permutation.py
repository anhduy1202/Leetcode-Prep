import copy
from unittest import result
def permutate(nums):
    result = []
    if len(nums) == 1:
        result.append(nums.copy())
    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permutate(nums)
        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)
    return result

print(permutate([1,2,3]))