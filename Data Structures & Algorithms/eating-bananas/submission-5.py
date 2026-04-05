class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        answer = 0
        while l <= r:
            mid = (l + r) // 2
            print(mid)
            time = 0
            for p in piles:
                time += math.ceil(p/mid)
            if time > h:
                l = mid + 1
            elif time <= h:
                r = mid - 1
                answer = mid
        return answer