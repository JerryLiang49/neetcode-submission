import math
class Solution:
    def canFinish(self, piles, h, k):
        time = 0
        for p in piles:
            time += math.ceil(p/k)
        return time <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, 1000000000
        ans = -1
        while left <= right:
            k = (left + right) // 2
            if self.canFinish(piles, h, k):
                right = k - 1
                ans = k
            else:
                left = k + 1
        return ans