class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1

            for j in range(1, amount + 1):
                nextDP[j] = dp[j]
                if j - coins[i] >= 0:
                    nextDP[j] += nextDP[j - coins[i]]
            dp = nextDP
            
        return dp[amount]