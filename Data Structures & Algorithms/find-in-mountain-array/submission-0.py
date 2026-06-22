class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        l = 0
        r = length - 1
        while l <= r:
            mid = (l + r) // 2
            left = mountainArr.get(mid - 1)
            middle = mountainArr.get(mid)
            right = mountainArr.get(mid + 1)

            if left < middle < right:
                l = mid + 1
            elif left > middle > right:
                r = mid - 1
            else:
                break
        peak = mid

        l = 0
        r = peak - 1
        while l <= r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)
            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                return mid
            
        l = peak
        r = length - 1
        while l <= r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)
            if val > target:
                l = mid + 1
            elif val < target:
                r = mid - 1
            else:
                return mid
            
        return -1