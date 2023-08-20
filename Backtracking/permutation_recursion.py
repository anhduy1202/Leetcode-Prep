import copy
def permute(nums):
    res = []
    n = len(nums)
    def permuteHelper(nums, chosen=[]):
        if len(chosen) == n:
            temp = chosen.copy()
            res.append(temp)
        else:
            # chose
            for i in range(len(nums)):
                s = nums[i]
                nums.pop(i)
                chosen.append(s)

                #explore
                permuteHelper(nums, chosen)

    permuteHelper(nums)
    return res

permute([1,3])