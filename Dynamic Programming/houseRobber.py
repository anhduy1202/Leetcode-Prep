def houseRobber(nums):
    rob1,rob2 = 0,0
    for num in nums:
        temp = max(rob1+num,rob2)
        rob1 = rob2
        rob2 = temp
    return rob2
print(houseRobber([2,1,1,2]))