class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)
        nums.sort()
        
        def dfs(i, path):
            if len(path) == len(nums):
                result.append(path.copy())
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                path.append(nums[i])
                used[i] = True
                dfs(i + 1, path)

                path.pop()
                used[i] = False
        
        dfs(0, [])
        return result
