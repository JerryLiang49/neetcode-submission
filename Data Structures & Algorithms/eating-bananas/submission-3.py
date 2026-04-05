class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1; r = max(piles)
        result = 0
        while l <= r:
            m = (l + r) // 2
            total = 0
            for p in piles:
                total += math.ceil(p/m)
            if total > h:
                l = m + 1
            elif total <= h:
                r = m - 1
                result = m
        return result