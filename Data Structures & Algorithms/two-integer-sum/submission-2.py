class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = dict()
        for i in range(len(nums)):
            find = target - nums[i]
            if find in prevMap:
                return [prevMap[find], i]
            prevMap[nums[i]] = i
        
        