class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        maxP = 0
        for j in range(1, len(prices)):
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                maxP = max(profit, maxP)
            else:
                i = j
        return maxP

