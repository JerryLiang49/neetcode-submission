class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        for j in range(1, len(prices)):
            if prices[j] > prices[i]:
                profit += prices[j] - prices[i]
                i = j
            else:
                i += 1
            
        return profit