class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num - 1 not in numSet:
                start = num
                length = 1
                while start + 1 in numSet:
                    length += 1
                    start += 1
                longest =  max(length, longest)
        return longest