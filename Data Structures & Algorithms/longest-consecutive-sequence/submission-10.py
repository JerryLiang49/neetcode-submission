class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxlength = 0
        for num in numsSet:
            if num - 1 not in numsSet:
                length = 1
                while num + length in numsSet:
                    length += 1
                maxlength = max(length, maxlength)
        return maxlength