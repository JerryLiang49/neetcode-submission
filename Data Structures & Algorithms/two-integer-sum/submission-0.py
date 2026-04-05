class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = dict()
        for index, value in enumerate(nums):
            find = target - value
            if find in prevMap:
                return [prevMap[find], index]
            prevMap[value] = index