class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse = True)
        subsets = [0] * k

        if sum(nums) % k:
            return False

        target = sum(nums) // k

        def dfs(index):
            if index == len(nums):
                return True
        
            for i in range(len(subsets)):
                if subsets[i] + nums[index] <= target:
                    subsets[i] += nums[index]
                    if dfs(index + 1):
                        return True
                    
                    subsets[i] -= nums[index]

                    if subsets[i] == 0:
                        break
                    
            return False

        return dfs(0)