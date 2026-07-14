class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minHeap = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(minHeap)
        maxProfit = []

        for _ in range(k):
            while minHeap and minHeap[0][0] <= w:
                capital, profit = heapq.heappop(minHeap)
                heapq.heappush(maxProfit, -profit)
            
            if not maxProfit:
                break

            w += -heapq.heappop(maxProfit)

        return w
                
            