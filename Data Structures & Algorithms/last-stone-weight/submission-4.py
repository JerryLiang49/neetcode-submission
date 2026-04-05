from heapq import heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            largest = -heappop(stones)
            second = -heappop(stones)
            if largest > second:
                heappush(stones, -(largest - second))
        
        return -stones[0] if len(stones) == 1 else 0