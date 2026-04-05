class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        maxP = 0
        for j in range(1, len(prices)):
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                maxP = max(maxP, profit)
            else:
                i = j
        return maxP