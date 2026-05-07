class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = [[0] * (sum(nums) + 1) for _ in range(len(nums))]
        
        def dfs(i, curr):
            if i == len(nums):
                if curr == target:
                    return 1
                else:
                    return 0
            if memo[i][curr] != 0:
                return memo[i][curr]
            
            memo[i][curr] = dfs(i + 1, curr - nums[i]) + dfs(i + 1, curr + nums[i])
        
            return memo[i][curr]
        
        return dfs(0, 0)