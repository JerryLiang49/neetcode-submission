class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        for num in nums:
            length = 0
            if num - 1 not in numsSet: # start of a sequence
                length = 1
                while num + length in numsSet:
                    length += 1
            longest = max(longest, length)
        return longest
