class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        result = 0

        def finish(piles, speed):
            time = 0
            for p in piles:
                time += math.ceil(p/speed)
            return time

        while l <= r:
            speed = (l + r) // 2
            if finish(piles, speed) > h:
                l = speed + 1
            elif finish(piles, speed) <= h:
                result = speed
                r = speed - 1
        
        return result