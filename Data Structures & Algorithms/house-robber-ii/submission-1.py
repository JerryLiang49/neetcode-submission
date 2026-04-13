class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo1 = [-1] * len(nums)
        memo2 = [-1] * len(nums)

        def dfs(i, end, memo):
            if i >= end:
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(nums[i] + dfs(i + 2, end, memo), dfs(i + 1, end, memo))
            return memo[i]
        
        res1 = dfs(0, len(nums) - 1, memo1)
        res2 = dfs(1, len(nums), memo2)

        return max(res1, res2)