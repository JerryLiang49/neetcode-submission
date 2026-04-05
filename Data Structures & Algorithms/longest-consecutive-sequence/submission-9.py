class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxlength = 0
        length = 1
        for num in numsSet:
            print("num:", num)
            if num - 1 not in numsSet:
                while num + length in numsSet:
                    print(num+length)
                    length += 1
                maxlength = max(length, maxlength)
                length = 0
            print("maxlength:", maxlength)
        return maxlength