class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        i = 0; j = 1
        for j in range(len(prices)):
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                maxProfit = max(profit, maxProfit)
            else:
                i = j
            j += 1
        return maxProfit