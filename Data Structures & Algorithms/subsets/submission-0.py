class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def dfs(index, path):
            result.append(path[:])
            for i in range(index, len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()
            
        dfs(0, [])
        return result