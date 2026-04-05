class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0; j = len(nums) - 1
        pivot = 0
        while i < j:
            m = (i + j) // 2
            if nums[m] > nums[j]:
                i = m + 1
            else:
                j = m
            pivot = i

        l = 0; r = len(nums) - 1
        m = (l + r) // 2
        if target >= nums[pivot] and target <= nums[r]:
            print("ho")
            l = pivot
        else:
            r = pivot - 1
        
        while l <= r:
            m = (l + r) // 2
            print(m)
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1