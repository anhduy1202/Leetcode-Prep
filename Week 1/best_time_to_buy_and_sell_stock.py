class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = float('inf')
        maxProf = 0
        for price in prices:
            if price < min:
                min = price
            maxProf = max(maxProf, price-min)
        return maxProf
