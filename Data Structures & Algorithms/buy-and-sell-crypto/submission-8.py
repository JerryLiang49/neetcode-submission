class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        profit = 0
        while j < len(prices):
            if prices[j] < prices[i]:
                i = j
                j = i + 1
            if j != len(prices):
                profit = max(profit, prices[j] - prices[i])
                j += 1
        return profit