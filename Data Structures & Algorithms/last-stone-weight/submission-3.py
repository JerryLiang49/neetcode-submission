from heapq import heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]

        maxheap = []

        for stone in stones:
            heappush(maxheap, -stone)
        
        while len(maxheap) > 1:
            largest = -heappop(maxheap)
            second = -heappop(maxheap)
            if largest == second:
                continue
            elif largest > second:
                heappush(maxheap, -(largest - second))
        
        return -maxheap[0] if len(maxheap) == 1 else 0