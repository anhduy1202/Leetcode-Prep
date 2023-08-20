import copy


def subsets(nums):
    res = []

    def subsetsHelper(av, chosen=[]):
        # base case
        if len(av) == 0:
            temp = chosen.copy()
            res.append(temp)
        else:
            # all possible choice
            element = av[0]
            av.pop(0)
            # chose/explore without [chosen]
            subsetsHelper(av, chosen)
            # choose/explore with [chosen]
            chosen.append(element)
            subsetsHelper(av, chosen)
            # un-choose
            av.insert(0, element)
            chosen.pop()

    subsetsHelper(nums, [])
    return res

res = subsets([1,2,3])
print(res)