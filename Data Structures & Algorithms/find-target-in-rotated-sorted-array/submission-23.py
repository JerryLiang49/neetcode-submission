class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid
        index = r
                
        if target == nums[r]:
            return r
        
        
        if target > nums[-1]:
            l = 0
        else:
            l = r
            r = len(nums) - 1
            
        print(l, r)

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
            
        return -1
        