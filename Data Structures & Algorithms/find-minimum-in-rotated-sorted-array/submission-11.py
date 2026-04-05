class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        curr = nums[0]
        while i < j:
            mid = (i + j) // 2
            print(nums[mid], mid)
            if nums[mid] > nums[j]:
                i = mid + 1
            else:
                curr = nums[mid]
                j = mid
        return nums[i]

