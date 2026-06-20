class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def split(largest):
            curr = 0
            splits = 0
            for num in nums:
                curr += num
                if curr > largest:
                    splits += 1
                    curr = num
            return splits + 1
        
        l = max(nums)
        r = sum(nums)
        while l <= r:
            mid = (l + r) // 2
            splits = split(mid)
            print(mid, splits)
            if splits > k:
                l = mid + 1
            else:
                result = mid
                r = mid - 1
        
        return result