from TreeNode import TreeNode
# Using divide conquer method: O(NlogN)
def buildBST(nums):
    if len(nums) < 1:
        return
    middle = len(nums) // 2
    root = TreeNode(nums[middle])
    root.left = buildBST(nums[:middle])
    root.right = buildBST(nums[middle+1:])
    return root

# Using 2 pointers Binary Search method: O(logN)
def buildBST2(nums):
    
    def binaryMerge(nums, lower, upper): 
        if lower == upper: 
            return
        middle  = ( lower + upper ) // 2
        root = TreeNode(nums[middle])
        root.left = binaryMerge(nums, lower, middle)
        root.right = binaryMerge(nums, middle + 1, upper)
        return root
    
    return binaryMerge(nums, 0, len(nums))
    

print(buildBST2([-10,-3,0,5,9]))    
