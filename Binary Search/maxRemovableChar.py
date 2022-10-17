
'''
1. We use Binary Search to optimize our searching for removable
2. EX: removable = [0,3,1,5], middle will be at index 2 => 1

Explanation ( why use BS ):

    We'll use set[:middle + 1] such that we currently removed all 
    the characters up until our middle point and with our helper function isSubSeq
    we can decide whether to remove even MORE characters by going to the RIGHT
    or remove LESS character by going to the LEFT
    that's why Binary Search can be applied for this problem
'''
def maximumRemovals(s, p, removable):
    def isSubSeq(s,subS):
        s1, subS1 = 0,0
        while s1 < len(s) and subS1 < len(subS):
            if s1 in removed or s[s1] != subS[subS1]:
                s1 += 1
                continue
            subS1 += 1
            s1 += 1
        return subS1 == len(subS)
    
    res = 0
    low,high = 0, len(removable) - 1
    while low <= high:
        middle = (low + high) // 2
        removed = set(removable[:middle+1])
        if isSubSeq(s,p):
            res = max(res, middle + 1)
            # be greedy and look for removing more characters
            low = middle + 1
        else:
            high = middle - 1
    return res


print(maximumRemovals("abcacb","ab",[3,1,0]))
