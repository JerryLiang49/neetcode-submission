class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(path, i, curr):
            if i == len(nums):
                if curr == target:
                    result.append(path[:])
                return

            if curr > target:
                return 
            
            path.append(nums[i])
            dfs(path, i, curr + nums[i])

            path.pop()
            dfs(path, i + 1, curr)
        
        dfs([], 0, 0)
        return result