class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        curr = 0
        minimal = float("inf")
        for j in range(len(nums)):
            curr += nums[j]
            while curr >= target:
                length = j - i + 1
                minimal = min(minimal, length)
                curr -= nums[i]
                i += 1
            
        return minimal if minimal != float("inf") else 0
