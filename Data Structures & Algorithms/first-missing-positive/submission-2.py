class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] <= 0 or nums[i] > len(nums):
                i += 1
                continue
            
            index = nums[i] - 1
            if nums[i] != nums[index]:
                nums[i], nums[index] = nums[index], nums[i]
            else:
                i += 1
            
        print(nums)
        result = 1
        for num in nums:
            if num != result:
                return result
            result += 1
        return result