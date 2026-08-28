class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def dfs(index, path):
            result.append(path[:])

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                
                path.append(nums[i])
                dfs(i + 1, path)

                path.pop()

        dfs(0, [])
        return result
