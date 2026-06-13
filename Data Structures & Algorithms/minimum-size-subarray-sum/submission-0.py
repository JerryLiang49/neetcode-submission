class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        i = 0
        curr = 0
        minimal = float("inf")
        for j in range(len(nums)):
            curr += nums[j]
            while curr >= target:
                length = j - i + 1
                print(length)
                minimal = min(minimal, length)
                print(minimal)
                curr -= nums[i]
                i += 1
            
        return minimal
