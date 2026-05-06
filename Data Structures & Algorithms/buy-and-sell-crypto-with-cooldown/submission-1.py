class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices) + 1)]

        for i in range(len(prices) -1, -1, -1):
            for buying in [True, False]:
                if buying:
                    buy = dp[i + 1][False] - prices[i] if i + 1 < len(prices) else -prices[i]
                    cooldown = dp[i + 1][True] if i + 1 < len(prices) else 0
                    dp[i][1] = max(buy, cooldown)
                else:
                    sell = dp[i + 2][True] + prices[i] if i + 2 < len(prices) else prices[i]
                    cooldown = dp[i + 1][False] if i + 1 < len(prices) else 0
                    dp[i][0] = max(sell, cooldown)
                
        return dp[0][1]