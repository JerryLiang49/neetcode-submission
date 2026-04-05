class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        l = 0; r = len(nums) - 1 
        while l <= r:
            if nums[l] < nums[r]:
                minimum = min(nums[l], minimum)
                break
            
            m = (l + r) // 2
            minimum = min(nums[m], minimum)
            if nums[m] >= nums[l]:
                l = m + 1
            elif nums[m] < nums[l]:
                r = m - 1
            else:
                return minimum
        return minimum