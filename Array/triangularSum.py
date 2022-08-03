def triangularSum(nums):
    def sum(nums,n):
            if n == 1:
                return nums[0]
            for i in range(n-1):
                nums[i] = (nums[i] + nums[i+1])%10
            return sum(nums,n-1)
        
    return sum(nums,len(nums))

print(triangularSum([1,2,3,4,5]))