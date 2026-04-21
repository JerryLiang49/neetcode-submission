class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [-1] * n
        
        def dfs(i):
            if i == len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]

            lis = 1
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    lis = max(lis, 1 + dfs(j))

            memo[i] = lis
            return lis
        
        return max(dfs(i) for i in range(n))
                

