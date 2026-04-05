class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        i = 0; j = 1
        # sliding window
        while j < len(prices):
            # slide right pointer
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                maxProfit = max(profit, maxProfit)
            else:
                # increment both pointers
                i = j
            j += 1
        return maxProfit