class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1; r = max(piles)
        result = 0
        while l <= r:
            mid = l + (r - l) // 2
            total = 0
            for pile in piles:
                time = math.ceil(pile/mid)
                total += time
            if total > h:
                l = mid + 1
            elif total <= h:
                r = mid - 1
                result = mid
        return result
        