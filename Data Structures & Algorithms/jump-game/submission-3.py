class Solution:
    def canJump(self, nums: List[int]) -> bool:

        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            jump = nums[i] + 1
            for j in range(1, jump):
                if i + j == goal:
                    goal = i
        
        return goal == 0