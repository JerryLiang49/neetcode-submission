class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(index, path, remaining):
            if remaining == 0:
                result.append(path[:])
                return
            
            for i in range(index, len(nums)):

                if remaining < 0:
                    continue

                path.append(nums[i])
                dfs(i, path, remaining - nums[i])
                path.pop()
            
        dfs(0, [], target)
        return result
