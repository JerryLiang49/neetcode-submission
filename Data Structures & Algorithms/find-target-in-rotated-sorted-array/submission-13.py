class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = self.findMin(nums)
        if nums[index] == target:
            return index
        l = index
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                break
        
        if nums[mid] != target:
            l = 0
            r = index
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    break
                
        if nums[mid] != target:
            return -1
        return mid
    
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        index = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid - 1
                index = mid
        return index