class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        i = 0; j = 1
        while j < len(prices):
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                result = max(result, profit)
            else:
                i = j
            j += 1
        return result