class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        for num in nums:
            if num:
                product *= num
            else:
                zeros += 1
        if zeros > 1: return [0] * len(nums)

        result = [0] * len(nums)
        for i in range(len(nums)):
            if zeros:
                if nums[i] == 0:
                    result[i] = product
            else:
                result[i] = product // nums[i]
        return result