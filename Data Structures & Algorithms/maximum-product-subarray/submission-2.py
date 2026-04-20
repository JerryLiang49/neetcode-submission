class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        currMax, currMin = 1, 1

        for num in nums:
            temp = currMax * num
            currMax = max(temp, num * currMin, num)
            currMin = min(num, currMin * num, temp)
            result = max(result, currMax)
        
        return result