class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(i, curr, curr_sum):
            if curr_sum == target:
                result.append(curr.copy())
                return

            if i == len(nums) or curr_sum > target:
                return
            
            curr.append(nums[i])
            dfs(i, curr, curr_sum + nums[i])

            curr.pop()
            dfs(i + 1, curr, curr_sum)
        
        dfs(0, [], 0)
        return result