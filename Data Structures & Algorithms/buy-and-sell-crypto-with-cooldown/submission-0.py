class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = dict()
        
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            cooldown = dfs(i + 1, buying)

            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                memo[(i, buying)] = max(buy, cooldown)
                return memo[(i, buying)]
            if not buying:
                buy = dfs(i + 2, not buying) + prices[i]
                memo[(i, buying)] = max(buy, cooldown)
                return memo[(i, buying)]
            
        return dfs(0, True)