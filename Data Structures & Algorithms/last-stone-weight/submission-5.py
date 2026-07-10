class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while stones:
            if len(stones) == 1:
                return -stones[0]
            
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            if first == second:
                continue
            if first > second:
                heapq.heappush(stones, -(first - second))
            
        return 0