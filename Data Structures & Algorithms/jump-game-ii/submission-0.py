class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        furthest = 0
        jumps = 0
        while l <= r:
            if r >= len(nums) - 1:
                break
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])
            jumps += 1
            l = r + 1
            r = furthest
        return jumps