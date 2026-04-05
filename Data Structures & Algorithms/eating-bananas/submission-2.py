class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1; r = max(piles)
        result = 0
        while l <= r:
            speed = (l + r) // 2
            time = 0
            for p in piles:
                time += math.ceil(p/speed)
            if time > h:
                l = speed + 1
            elif time <= h:
                r = speed - 1
                result = speed
        return result