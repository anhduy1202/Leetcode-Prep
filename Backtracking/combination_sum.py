from collections import Counter
def combinationSum(candidates, target):
    res = []
    # Use index to refer the element of array since we dont want to repeat the same combination
    def combinationSumHelper(chosen, i, total):
        # base case
        if total == target:
            res.append(chosen.copy())
        # out of range
        elif total > target or i > len(candidates)-1:
            return
        else:
            # choose
            element = candidates[i]
            chosen.append(element)
            # explore
            combinationSumHelper(chosen, i, total+element)
            chosen.pop()
            combinationSumHelper(chosen, i+1, total)

    combinationSumHelper([], 0, 0)
    return res

res = combinationSum([1, 3], 3)
print(res)