def Knapsack(weights,profits,capacity,currentIdx):
    if capacity <= 0 or currentIdx >= len(profits):
        return 0
    
    profit1 = 0
    #Choose element at current index
    if weights[currentIdx] <= capacity:
        profit1 = profits[currentIdx] + Knapsack(weights,profits,capacity-weights[currentIdx], currentIdx+1)
    
    profit2 = Knapsack(weights,profits,capacity,currentIdx+1)


    return max(profit1,profit2)

print(Knapsack([2,3,1,4],[4,5,3,7],5,0))

