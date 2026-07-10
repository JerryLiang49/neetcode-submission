class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []

        for p in points:
            distance = p[0]**2 + p[1]**2
            heapq.heappush(heap, (distance, p[0], p[1]))
            
        while k:
            distance, x, y = heapq.heappop(heap)
            result.append([x, y])
            k -= 1
        
        return result